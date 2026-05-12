
"""
TP2 : Manipulation des caractères et conversions
Template à remplir par les élèves
"""

# ==================== DONNÉES DE TEST ====================
donnees = {
    "ex1_mot": "python",
    "ex2_mot": "programmation",
    "ex3_char": "A",
    "ex4_lettre": "B",
    "ex5_char": "5",
    "ex6_phrase": "Python3 est version 3.11",
    "ex7_chiffres": "1352",
    "ex8_nombre_text": "42",
    "ex9_texte": "123abc456",
    "ex10_num1": 12,
    "ex10_num2": 3,
    "ex11_nombre": 1234,
    "ex12_nombre": 5678,
    "ex13_expression": "12+3",
}

# ==================== EXERCICES ====================

# EXERCICE 1 : Parcourir une chaîne
# Créez une liste contenant chaque caractère du mot "python"
# Exemple résultat : ['p', 'y', 't', 'h', 'o', 'n']
mot = donnees["ex1_mot"]
resultat_ex1 = []
for caractere in mot:
    resultat_ex1.append(caractere)


# EXERCICE 2 : Position des caractères
# Affichez chaque lettre du mot "programmation" avec sa position
# Exemple résultat : "p:0 r:1 o:2 g:3..." (comme string ou dict)
mot = donnees["ex2_mot"]
resultat_ex2 = ""
index = 0
for caractere in mot:
    resultat_ex2 += caractere + ":" + str(index)
    if index < len(mot) - 1:
        resultat_ex2 += " "
    index += 1


# EXERCICE 3 : Codes des caractères
# Retournez le code ASCII d'un caractère avec ord()
char = donnees["ex3_char"]
# Code ASCII de "A"
resultat_ex3 = ord(char)


# EXERCICE 4 : Majuscule ou minuscule
# Utilisez le code ASCII pour déterminer si c'est majuscule ou minuscule
lettre = donnees["ex4_lettre"]
# Retournez "majuscule" ou "minuscule"
code_lettre = ord(lettre)
if 65 <= code_lettre <= 90:
    resultat_ex4 = "majuscule"
elif 97 <= code_lettre <= 122:
    resultat_ex4 = "minuscule"
else:
    resultat_ex4 = "autre"


# EXERCICE 5 : Est-ce un chiffre ?
# Utilisez le code ASCII pour vérifier si c'est un chiffre
char = donnees["ex5_char"]
# Retournez True ou False
code_char = ord(char)
resultat_ex5 = 48 <= code_char <= 57


# EXERCICE 6 : Compter les chiffres dans un texte
phrase = donnees["ex6_phrase"]
# Comptez combien de chiffres (0-9) la phrase contient
# Indice : ord('0') = 48, ord('9') = 57
resultat_ex6 = 0
for caractere in phrase:
    code_caractere = ord(caractere)
    if 48 <= code_caractere <= 57:
        resultat_ex6 += 1


# EXERCICE 7 : Somme des chiffres d'un texte
chiffres_text = donnees["ex7_chiffres"]
# Convertissez chaque caractère chiffre en nombre et additionnez
# "1352" → 1 + 3 + 5 + 2 = 11
resultat_ex7 = 0
for caractere in chiffres_text:
    resultat_ex7 += ord(caractere) - ord("0")


# EXERCICE 8 : Construire un nombre
# Lisez un nombre texte caractère par caractère
# Utilisez la formule : resultat = resultat * 10 + chiffre
nombre_text = donnees["ex8_nombre_text"]
# Convertissez "42" en nombre 42 (sans utiliser int())
resultat_ex8 = 0
for caractere in nombre_text:
    resultat_ex8 = resultat_ex8 * 10 + (ord(caractere) - ord("0"))


# EXERCICE 9 : Vérifier une entrée numérique
texte = donnees["ex9_texte"]
# Vérifiez si le texte ne contient QUE des chiffres
# "123abc456" → False (contient des lettres)
# "123456" → True
resultat_ex9 = True
for caractere in texte:
    code_caractere = ord(caractere)
    if code_caractere < 48 or code_caractere > 57:
        resultat_ex9 = False
        break


# EXERCICE 10 : Mini addition de nombres texte
num1_text = str(donnees["ex10_num1"])  # "12"
num2_text = str(donnees["ex10_num2"])  # "3"
# Convertissez manuellement en nombres (sans int())
# puis additionnez et retournez le résultat
valeur1 = 0
for caractere in num1_text:
    valeur1 = valeur1 * 10 + (ord(caractere) - ord("0"))
valeur2 = 0
for caractere in num2_text:
    valeur2 = valeur2 * 10 + (ord(caractere) - ord("0"))
resultat_ex10 = valeur1 + valeur2


# EXERCICE 11 : Extraire les chiffres d'un nombre
nombre = donnees["ex11_nombre"]
# Affichez les chiffres un par un en utilisant % et //
# 1234 → ['1', '2', '3', '4'] ou "1234"
resultat_ex11 = []
if nombre == 0:
    resultat_ex11.append("0")
else:
    temp = nombre
    while temp > 0:
        chiffre = temp % 10
        resultat_ex11.append(chr(ord("0") + chiffre))
        temp //= 10
    resultat_ex11.reverse()


# EXERCICE 12 : Inverser un nombre
nombre = donnees["ex12_nombre"]
# Affichez le nombre avec chiffres inversés
# 5678 → 8765
resultat_ex12 = 0
temp = nombre
while temp > 0:
    resultat_ex12 = resultat_ex12 * 10 + (temp % 10)
    temp //= 10


# EXERCICE 13 : Bonus - Calculatrice simple
expression = donnees["ex13_expression"]
# Parsez une expression comme "12+3"
# Identifiez les nombres et l'opérateur
# Retournez le résultat du calcul
# "12+3" → 15
operateur = ""
partie_gauche = ""
partie_droite = ""
avant_operateur = True
for caractere in expression:
    if caractere == "+" or caractere == "-" or caractere == "*" or caractere == "/":
        operateur = caractere
        avant_operateur = False
    elif avant_operateur:
        partie_gauche += caractere
    else:
        partie_droite += caractere
valeur_gauche = 0
for caractere in partie_gauche:
    valeur_gauche = valeur_gauche * 10 + (ord(caractere) - ord("0"))
valeur_droite = 0
for caractere in partie_droite:
    valeur_droite = valeur_droite * 10 + (ord(caractere) - ord("0"))
if operateur == "+":
    resultat_ex13 = valeur_gauche + valeur_droite
elif operateur == "-":
    resultat_ex13 = valeur_gauche - valeur_droite
elif operateur == "*":
    resultat_ex13 = valeur_gauche * valeur_droite
elif operateur == "/":
    resultat_ex13 = valeur_gauche / valeur_droite
else:
    resultat_ex13 = None
