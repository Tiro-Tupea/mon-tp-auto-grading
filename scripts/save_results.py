"""
save_results.py - Lance pytest par élève et enregistre les résultats dans PostgreSQL
"""

import os
import re
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime
import psycopg2

DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', '5432')),
    'user': os.getenv('DB_USER', 'tp_user'),
    'password': os.getenv('DB_PASSWORD', 'tp_password'),
    'database': os.getenv('DB_NAME', 'tp_grading'),
}

TESTS_DIR = Path("tests")
ELEVES_DIR = Path("eleves")


def connect_db():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except psycopg2.Error as e:
        print(f"❌ Connexion BD échouée : {e}")
        return None


def get_or_create_student(cursor, student_name, group_name):
    cursor.execute("SELECT id FROM eleves WHERE nom = %s", (student_name,))
    row = cursor.fetchone()
    if row:
        return row[0]
    email = f"{student_name.replace(' ', '.').lower()}@cf2m.be"
    cursor.execute(
        "INSERT INTO eleves (nom, email) VALUES (%s, %s) RETURNING id",
        (student_name, email)
    )
    return cursor.fetchone()[0]


def run_pytest_for_student(student_dir: Path, tp_name: str) -> dict:
    """
    Lance pytest pour un TP d'un élève.
    Retourne un dict {exercice_num: 'PASSED' | 'FAILED' | 'NOT_DONE'}.
    """
    test_file = TESTS_DIR / f"test_{tp_name}.py"
    if not test_file.exists():
        return {}

    # Copie temporaire pour que pytest importe le bon fichier
    tp_copy = student_dir / f"{tp_name}.py"
    src_file = student_dir / f"{tp_name}.py"
    if not src_file.exists():
        return {}

    try:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", str(test_file), "-v", "--tb=no", "-q"],
            capture_output=True,
            text=True,
            timeout=30,
            env={**os.environ, "PYTHONPATH": str(student_dir.resolve())},
        )
        output = result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        print(f"    ⏱ Timeout pour {tp_name}")
        return {}
    except Exception as e:
        print(f"    ⚠️ Erreur subprocess : {e}")
        return {}

    # Parser les lignes de résultat pytest : "PASSED tests/...::test_ex3_..." ou "FAILED ..."
    exercise_results = {}
    for line in output.splitlines():
        match = re.search(r'(PASSED|FAILED)\s+.*test_ex(\d+)', line)
        if match:
            status, ex_num = match.group(1), int(match.group(2))
            exercise_results[ex_num] = status

    return exercise_results


def save_results(conn, student_id, tp_name, exercise_results: dict):
    commit_sha = os.getenv('GITHUB_SHA', 'local')[:40]
    with conn.cursor() as cur:
        for ex_num, status in exercise_results.items():
            score = 1 if status == 'PASSED' else 0
            cur.execute("""
                INSERT INTO resultats
                    (eleve_id, tp_name, exercice_num, statut, score, commit_sha, date_test)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (eleve_id, tp_name, exercice_num, date_test)
                DO UPDATE SET statut = EXCLUDED.statut, score = EXCLUDED.score, commit_sha = EXCLUDED.commit_sha
            """, (student_id, tp_name, ex_num, status, score, commit_sha, datetime.utcnow()))
    conn.commit()


def iter_students():
    """Parcourt eleves/web1/ et eleves/web2/ et retourne (group, student_dir)."""
    for group_dir in sorted(ELEVES_DIR.iterdir()):
        if not group_dir.is_dir() or group_dir.name.startswith('.'):
            continue
        # Support structure plate (eleves/alice/) ET groupes (eleves/web1/alice/)
        has_subfolders = any(d.is_dir() for d in group_dir.iterdir())
        tp_files = list(group_dir.glob("tp*.py"))
        if tp_files:
            # Dossier élève direct
            yield group_dir.name, group_dir
        elif has_subfolders:
            for student_dir in sorted(group_dir.iterdir()):
                if student_dir.is_dir() and not student_dir.name.startswith('.'):
                    yield group_dir.name, student_dir


def main():
    print("\n" + "=" * 60)
    print("Auto-grading : tests + sauvegarde PostgreSQL")
    print("=" * 60)

    conn = connect_db()
    if not conn:
        sys.exit(1)

    if not ELEVES_DIR.exists():
        print("❌ Dossier 'eleves/' introuvable")
        sys.exit(1)

    total_passed = total_failed = 0

    for group_name, student_dir in iter_students():
        student_name = student_dir.name
        print(f"\n👤 [{group_name}] {student_name}")

        tp_files = sorted(student_dir.glob("tp*.py"))
        if not tp_files:
            print("   (aucun fichier TP)")
            continue

        with conn.cursor() as cur:
            student_id = get_or_create_student(cur, student_name, group_name)
        conn.commit()

        for tp_file in tp_files:
            tp_name = tp_file.stem
            print(f"  📝 {tp_name} ... ", end="", flush=True)

            results = run_pytest_for_student(student_dir, tp_name)

            if not results:
                print("⚠️  (aucun résultat)")
                continue

            passed = sum(1 for s in results.values() if s == 'PASSED')
            total = len(results)
            total_passed += passed
            total_failed += (total - passed)

            save_results(conn, student_id, tp_name, results)
            print(f"{'✅' if passed == total else '⚠️ '} {passed}/{total}")

    conn.close()

    print("\n" + "=" * 60)
    grand_total = total_passed + total_failed
    if grand_total:
        pct = total_passed / grand_total * 100
        print(f"📊 TOTAL : {total_passed}/{grand_total} ({pct:.0f}%)")
    print("=" * 60)


if __name__ == "__main__":
    main()
