"""
run_all_tests.py - Lance les tests pytest pour tous les élèves
Version 3 - VRAIMENT fonctionnelle
"""

import os
import sys
import subprocess
from pathlib import Path

def run_tests():
    """Lance les tests pour chaque élève"""
    
    print("="*60)
    print("🧪 Lancement des tests pour tous les élèves")
    print("="*60)
    
    eleves_dir = Path("eleves")
    tests_dir = Path("tests")
    
    if not eleves_dir.exists():
        print("❌ Dossier 'eleves' introuvable")
        return False
    
    if not tests_dir.exists():
        print("❌ Dossier 'tests' introuvable")
        return False
    
    total_passed = 0
    total_failed = 0
    
    # Parcourir chaque élève (supporte eleves/web1/alice/ ET eleves/alice/)
    def iter_students(base):
        for entry in sorted(base.iterdir()):
            if not entry.is_dir() or entry.name.startswith('.'):
                continue
            if list(entry.glob("tp*.py")):
                yield entry
            else:
                yield from iter_students(entry)

    for student_dir in iter_students(eleves_dir):
        student_name = student_dir.name
        print(f"\n👤 {student_name}")
        
        # Parcourir chaque TP
        tp_files = sorted(student_dir.glob("tp*.py"))
        
        for tp_file in tp_files:
            tp_name = tp_file.stem  # tp3, tp4, etc.
            
            # Chercher le fichier de test correspondant
            test_file = tests_dir / f"test_{tp_name}.py"
            
            if not test_file.exists():
                print(f"  ⚠️  {tp_name}: Pas de test trouvé")
                continue
            
            print(f"  📝 {tp_name}...", end=" ", flush=True)
            
            try:
                # Créer un fichier tp.py dans le dossier élève pour que pytest le trouve
                tp_link = student_dir / "tp.py"
                
                # Copier ou linker le fichier
                with open(tp_file, 'r') as src:
                    with open(tp_link, 'w') as dst:
                        dst.write(src.read())
                
                # Lancer pytest DEPUIS LE RÉPERTOIRE RACINE
                result = subprocess.run(
                    [sys.executable, "-m", "pytest", str(test_file), "-v", "--tb=short"],
                    capture_output=True,
                    text=True,
                    cwd=".",  # ← Depuis le répertoire racine
                    timeout=30,
                    env={**os.environ, "PYTHONPATH": str(student_dir)}
                )
                
                # Parser les résultats
                output = result.stdout + result.stderr
                
                # Compter les tests passés/échoués
                if "passed" in output:
                    # Chercher le résumé final
                    lines = output.split('\n')
                    for line in lines:
                        if "passed" in line or "failed" in line:
                            # Extraire les nombres
                            import re
                            passed_match = re.search(r'(\d+)\s+passed', line)
                            failed_match = re.search(r'(\d+)\s+failed', line)
                            
                            passed = int(passed_match.group(1)) if passed_match else 0
                            failed = int(failed_match.group(1)) if failed_match else 0
                            
                            if passed + failed > 0:
                                total_passed += passed
                                total_failed += failed
                                
                                if failed == 0:
                                    print(f"✓ ({passed} tests)")
                                else:
                                    print(f"⚠️  ({passed}/{passed+failed} tests)")
                                break
                else:
                    print(f"✗ (erreur)")
                
                # Nettoyer le fichier temporaire
                if tp_link.exists():
                    tp_link.unlink()
                    
            except subprocess.TimeoutExpired:
                print("✗ (timeout)")
            except Exception as e:
                print(f"✗ Erreur: {e}")
    
    # Résumé final
    print("\n" + "="*60)
    print("📊 RÉSUMÉ FINAL")
    print("="*60)
    
    total_tests = total_passed + total_failed
    if total_tests > 0:
        percentage = (total_passed / total_tests) * 100
        print(f"Total : {total_passed}/{total_tests} tests ({percentage:.0f}%)")
    else:
        print("Aucun test exécuté")
    
    print("="*60)
    
    return True


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)