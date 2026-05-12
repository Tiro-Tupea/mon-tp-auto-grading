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
for l in mot :
    resultat_ex1.append(l)


# EXERCICE 2 : Compter une lettre
mot = donnees["ex2_mot"]
lettre = donnees["ex2_lettre"]
# Comptez combien de fois la lettre "a" apparaît
compteur = 0 
for l in mot: 
    if l == lettre: 
        compteur += 1
resultat_ex2 = compteur


# EXERCICE 3 : Compter les voyelles
mot = donnees["ex3_mot"]
# Comptez les voyelles (a, e, i, o, u, y)
voyelles = "aieouy"
compteur = 0 
for l in mot: 
    for v in voyelles:
        if l == v:
            compteur += 1
resultat_ex3 = compteur


# EXERCICE 4 : Inverser une chaîne
mot = donnees["ex4_mot"]
# Affichez le mot à l'envers : "hello" → "olleh"
resultat_ex4 = ""
i = 0 
while i < len(mot):
    i += 1 
    resultat_ex4 += mot[len(mot) - i]


# EXERCICE 5 : Vérifier un palindrome
mot = donnees["ex5_mot"]
# Vérifiez si le mot se lit pareil dans les deux sens
# "radar" → True
inverse = ""
i = 0 
while i < len(mot):
    i += 1
    inverse += mot[len(mot) - i] 
resultat_ex5 = (mot == inverse)


# EXERCICE 6 : Compter les mots
phrase = donnees["ex6_phrase"]
# Comptez combien de mots la phrase contient (sans utiliser split)
compteur = 0
dans_mot = False
for l in phrase:
    if l != " " and not dans_mot:
        dans_mot = True
        compteur += 1
    elif l == " ": 
        dans_mot = False
resultat_ex6 = compteur


# EXERCICE 7 : Supprimer les espaces en début et fin
phrase = donnees["ex7_phrase"]
# Retournez la phrase sans espaces au début et fin
debut = 0 
fin = len(phrase) - 1
while debut <= fin and phrase[debut] == " ":
    debut += 1
while fin >= debut and phrase[fin] == " ":
    fin -= 1
resultat_ex7 = ""
i = debut
while i <= fin : 
    resultat_ex7 += phrase[i]
    i += 1

# EXERCICE 8 : Trouver le mot le plus long
phrase = donnees["ex8_phrase"]
# Retournez le mot le plus long de la phrase (sans utiliser split)
mot_courant = ""
mot_long = ""
for c in phrase:
    if c != " ":
        mot_courant += c
    else:
        if len(mot_courant) > len(mot_long):
            mot_long = mot_courant
        mot_courant = ""
# vérifier le dernier mot
if len(mot_courant) > len(mot_long):
    mot_long = mot_courant
resultat_ex8 = mot_long


# EXERCICE 9 : Supprimer les espaces multiples
phrase = donnees["ex9_phrase"]
# Transformez "Bonjour  tout   le    monde" en "Bonjour tout le monde"
resultat_ex9 = ""
espace = False
for e in phrase: 
    if e == " ":
        if not espace:
            resultat_ex9 += e
        espace = True
    else:
        resultat_ex9 += e
        espace = False

# EXERCICE 10 : Inverser les mots d'une phrase
phrase = donnees["ex10_phrase"]
# "Python est genial" → "genial est Python"
mots = []
mot_courant = ""
for m in phrase:
    if m != " ":
        mot_courant += m
    else:
        if mot_courant != "":
            mots.append(mot_courant)
        mot_courant = ""
if mot_courant != "":
    mots.append(mot_courant)

resultat_ex10 = ""
i = len(mots) - 1 
while i >= 0: 
    resultat_ex10 += mots[i]
    if i > 0: 
        resultat_ex10 += " "
    i -= 1

# EXERCICE 11 : Supprimer les caractères consécutifs identiques
chaine = donnees["ex11_chaine"]
# "booonnjooour" → "bonjour"
resultat_ex11 = ""
i = 0 
while i < len(chaine):
    if i == 0 or chaine[i] != chaine [i - 1]:
        resultat_ex11 += chaine[i]
    i += 1 


# EXERCICE 12 : Compression simple d'une chaîne
chaine = donnees["ex12_chaine"]
# "aaabbc" → "a3b2c1"
resultat_ex12 = ""
i = 0 
while i < len(chaine):
    c = chaine[i]
    compteur = 1
    while i + compteur < len(chaine) and chaine[i + compteur] == c:
        compteur += 1
    resultat_ex12 += c + str(compteur)
    i += compteur 


# EXERCICE 13 : Vérifier des parenthèses équilibrées
expression = donnees["ex13_expression"]
# Vérifiez si les parenthèses sont correctement équilibrées
# "(a + b) * (c - d)" → True
compteur = 0 
resultat_ex13 = True
for c in expression: 
    if c == "(":
        compteur +=1 
    elif c ==")": 
        compteur -= 1
    if compteur < 0 : 
        resultat_ex13 = False
if compteur != 0: 
    resultat_ex13 = False

# EXERCICE 14 : Vérifier deux anagrammes
mot1 = donnees["ex14_mot1"]
mot2 = donnees["ex14_mot2"]
# Vérifiez si les deux mots sont des anagrammes
# "listen" et "silent" → True
if len(mot1) != len(mot2):
    resultat_ex14 = False
else: 
    lettre = []
    for c in mot2:
        lettre.append(c)
    resultat_ex14 = True
    for c in mot1:
        trouve = False
        i = 0
        while i < len(lettre):
            if lettre[i] == c:
                lettre[i] = None
                trouve = True
                break 
            i += 1
        if not trouve: 
            resultat_ex14 = False


# EXERCICE 15 : Mini analyseur de phrase
phrase = donnees["ex15_phrase"]
# Retournez un dictionnaire avec :
# - "nombre_mots": nombre de mots
# - "mot_le_plus_long": le mot le plus long
# - "nombre_caracteres": nombre total de caractères (sans espaces)
mots = []
mot_courant = ""
for c in phrase:
    if c != " ":
        mot_courant += c
    else:
        if mot_courant != "":
            mots.append(mot_courant)
        mot_courant = ""
if mot_courant != "":
    mots.append(mot_courant)

nombre_mots = 0
for m in mots:
    nombre_mots += 1

mot_long = ""
for m in mots:
    if len(m) > len(mot_long):
        mot_long = m

nb_chars = 0
for c in phrase:
    if c != " ":
        nb_chars += 1

resultat_ex15 = {
    "nombre_mots": nombre_mots,
    "mot_le_plus_long": mot_long,
    "nombre_caracteres": nb_chars
}