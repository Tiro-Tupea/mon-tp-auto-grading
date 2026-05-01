
"""
TP3 : Algorithmique sur les chaînes de caractères
Template à remplir par les élèves
"""

donnees = {
    "ex1_mot": "algorithmique",
    "ex2_mot": "programmation",
    "ex2_lettre": "a",
    "ex3_mot": "bonjour",
    "ex4_mot": "hello",
    "ex5_mot": "radar",
    "ex6_phrase": "Bonjour tout le monde",
    "ex7_phrase": "  Bonjour le monde  ",
    "ex8_phrase": "Bonjour tout le monde",
    "ex9_phrase": "Bonjour  tout   le    monde",
    "ex10_phrase": "Python est genial",
    "ex11_chaine": "booonnjooour",
    "ex12_chaine": "aaabbc",
    "ex13_expression": "(a + b) * (c - d)",
    "ex14_mot1": "listen",
    "ex14_mot2": "silent",
    "ex15_phrase": "Bonjour tout le monde avec tous",
}

# ==================== EXERCICES ====================

# EXERCICE 1 : Parcourir une chaîne
# Créez une liste avec chaque caractère du mot "algorithmique"
mot = donnees["ex1_mot"]
resultat_ex1 = []
for caractere in mot:
    resultat_ex1.append(caractere)


# EXERCICE 2 : Compter une lettre
mot = donnees["ex2_mot"]
lettre = donnees["ex2_lettre"]
# Comptez combien de fois la lettre "a" apparaît
resultat_ex2 = 0
for caractere in mot:
    if caractere == lettre:
        resultat_ex2 += 1


# EXERCICE 3 : Compter les voyelles
mot = donnees["ex3_mot"]
# Comptez les voyelles (a, e, i, o, u, y)
resultat_ex3 = 0
for caractere in mot:
    if caractere in "aeiouy":
        resultat_ex3 += 1


# EXERCICE 4 : Inverser une chaîne
mot = donnees["ex4_mot"]
# Affichez le mot à l'envers : "hello" → "olleh"
resultat_ex4 = ""
index = len(mot) - 1
while index >= 0:
    resultat_ex4 += mot[index]
    index -= 1


# EXERCICE 5 : Vérifier un palindrome
mot = donnees["ex5_mot"]
# Vérifiez si le mot se lit pareil dans les deux sens
# "radar" → True
inverse = ""
index = len(mot) - 1
while index >= 0:
    inverse += mot[index]
    index -= 1
resultat_ex5 = inverse == mot


# EXERCICE 6 : Compter les mots
phrase = donnees["ex6_phrase"]
# Comptez combien de mots la phrase contient (sans utiliser split)
resultat_ex6 = 0
dans_mot = False
for caractere in phrase:
    if caractere != " ":
        if not dans_mot:
            resultat_ex6 += 1
            dans_mot = True
    else:
        dans_mot = False


# EXERCICE 7 : Supprimer les espaces en début et fin
phrase = donnees["ex7_phrase"]
# Retournez la phrase sans espaces au début et fin
start = 0
while start < len(phrase) and phrase[start] == " ":
    start += 1
end = len(phrase) - 1
while end >= 0 and phrase[end] == " ":
    end -= 1
if start <= end:
    resultat_ex7 = phrase[start:end + 1]
else:
    resultat_ex7 = ""


# EXERCICE 8 : Trouver le mot le plus long
phrase = donnees["ex8_phrase"]
# Retournez le mot le plus long de la phrase (sans utiliser split)
resultat_ex8 = ""
mot_courant = ""
for caractere in phrase:
    if caractere != " ":
        mot_courant += caractere
    else:
        if mot_courant != "" and len(mot_courant) > len(resultat_ex8):
            resultat_ex8 = mot_courant
        mot_courant = ""
if mot_courant != "" and len(mot_courant) > len(resultat_ex8):
    resultat_ex8 = mot_courant


# EXERCICE 9 : Supprimer les espaces multiples
phrase = donnees["ex9_phrase"]
# Transformez "Bonjour  tout   le    monde" en "Bonjour tout le monde"
resultat_ex9 = ""
espace_precedent = False
for caractere in phrase:
    if caractere == " ":
        if not espace_precedent:
            resultat_ex9 += " "
            espace_precedent = True
    else:
        resultat_ex9 += caractere
        espace_precedent = False


# EXERCICE 10 : Inverser les mots d'une phrase
phrase = donnees["ex10_phrase"]
# "Python est genial" → "genial est Python"
mots = []
mot_courant = ""
for caractere in phrase:
    if caractere != " ":
        mot_courant += caractere
    else:
        if mot_courant != "":
            mots.append(mot_courant)
            mot_courant = ""
if mot_courant != "":
    mots.append(mot_courant)
resultat_ex10 = ""
index = len(mots) - 1
while index >= 0:
    resultat_ex10 += mots[index]
    if index > 0:
        resultat_ex10 += " "
    index -= 1


# EXERCICE 11 : Supprimer les caractères consécutifs identiques
chaine = donnees["ex11_chaine"]
# "booonnjooour" → "bonjour"
resultat_ex11 = ""
precedent = ""
for caractere in chaine:
    if caractere != precedent:
        resultat_ex11 += caractere
    precedent = caractere


# EXERCICE 12 : Compression simple d'une chaîne
chaine = donnees["ex12_chaine"]
# "aaabbc" → "a3b2c1"
resultat_ex12 = ""
compte = 1
index = 1
while index < len(chaine):
    if chaine[index] == chaine[index - 1]:
        compte += 1
    else:
        resultat_ex12 += chaine[index - 1] + str(compte)
        compte = 1
    index += 1
if len(chaine) > 0:
    resultat_ex12 += chaine[-1] + str(compte)


# EXERCICE 13 : Vérifier des parenthèses équilibrées
expression = donnees["ex13_expression"]
# Vérifiez si les parenthèses sont correctement équilibrées
# "(a + b) * (c - d)" → True
compteur = 0
equilibre = True
for caractere in expression:
    if caractere == "(":
        compteur += 1
    elif caractere == ")":
        compteur -= 1
    if compteur < 0:
        equilibre = False
        break
resultat_ex13 = equilibre and compteur == 0


# EXERCICE 14 : Vérifier deux anagrammes
mot1 = donnees["ex14_mot1"]
mot2 = donnees["ex14_mot2"]
# Vérifiez si les deux mots sont des anagrammes
# "listen" et "silent" → True
resultat_ex14 = False
if len(mot1) == len(mot2):
    comptes1 = {}
    comptes2 = {}
    for caractere in mot1:
        if caractere in comptes1:
            comptes1[caractere] += 1
        else:
            comptes1[caractere] = 1
    for caractere in mot2:
        if caractere in comptes2:
            comptes2[caractere] += 1
        else:
            comptes2[caractere] = 1
    egal = True
    for caractere in comptes1:
        if caractere not in comptes2 or comptes1[caractere] != comptes2[caractere]:
            egal = False
            break
    for caractere in comptes2:
        if caractere not in comptes1:
            egal = False
            break
    resultat_ex14 = egal


# EXERCICE 15 : Mini analyseur de phrase
phrase = donnees["ex15_phrase"]
# Retournez un dictionnaire avec :
# - "nombre_mots": nombre de mots
# - "mot_le_plus_long": le mot le plus long
# - "nombre_caracteres": nombre total de caractères (sans espaces)
nombre_mots = 0
mot_le_plus_long = ""
nombre_caracteres = 0
mot_courant = ""
for caractere in phrase:
    if caractere != " ":
        mot_courant += caractere
        nombre_caracteres += 1
    else:
        if mot_courant != "":
            nombre_mots += 1
            if len(mot_courant) > len(mot_le_plus_long):
                mot_le_plus_long = mot_courant
            mot_courant = ""
if mot_courant != "":
    nombre_mots += 1
    if len(mot_courant) > len(mot_le_plus_long):
        mot_le_plus_long = mot_courant
resultat_ex15 = {
    "nombre_mots": nombre_mots,
    "mot_le_plus_long": mot_le_plus_long,
    "nombre_caracteres": nombre_caracteres,
}
