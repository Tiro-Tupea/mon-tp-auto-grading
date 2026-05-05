"""
TP1 : Introduction à Python
Template à remplir par les élèves
"""

# ==================== DONNÉES DE TEST ====================
# NE PAS MODIFIER - Les données utilisées pour les tests

donnees = {
    "ex3_a": 5,
    "ex3_b": 3,
    "ex5_prenom": "Alice",
    "ex5_nom": "Dupont",
    "ex6_x": 7,
    "ex6_y": 8,
    "ex7_a": 10,
    "ex7_b": 3,
    "ex8_dividende": 15,
    "ex8_diviseur": 4,
    "ex9_age": "25",
    "ex10_valeur": 3.14,
    "ex11_texte": "formation python",
    "ex12_phrase": "Bonjour le monde",
    "ex13_celsius": 0,
    "ex14_num1": 12,
    "ex14_num2": 5,
}

# ==================== EXERCICES ====================

# EXERCICE 1 : Afficher un message
# Affichez : "Bienvenue dans la formation Python !"
resultat_ex1 = "Bienvenue dans la formation Python !"
print (resultat_ex1)


# EXERCICE 2 : Afficher plusieurs lignes
# Affichez sur 3 lignes :
# Bonjour !
# Bienvenue dans le monde de la programmation Python.
# Amusez-vous bien !
resultat_ex2 = """Bonjour !"
Bienvenue dans le monde de la programmation Python."
Amusez-vous bien !"""

print (resultat_ex2)

# EXERCICE 3 : Addition simple
# Créez deux variables a et b avec les données
a = donnees["ex3_a"]
b = donnees["ex3_b"]
# Calculez la somme
resultat_ex3 = donnees["ex3_a"] + donnees["ex3_b"]
print(resultat_ex3)


# EXERCICE 4 : Créer et afficher une variable
# Créez une variable nom et mettez-y "Alice"
# Affichez : "Bonjour, Alice !"
nom = "Alice"
resultat_ex4 = "Bonjour, "
print( resultat_ex4, nom + " !")


# EXERCICE 5 : Concaténation de chaînes
# Utilisez les données
prenom = donnees["ex5_prenom"]
nom = donnees["ex5_nom"]
# Créez le message : "Bonjour, [prénom] [nom] !"
resultat_ex5 = prenom +" "+ nom
print(resultat_ex5)

# EXERCICE 6 : Multiplier des nombres
x = donnees["ex6_x"]
y = donnees["ex6_y"]
# Calculez le produit
resultat_ex6 = x * y
print(resultat_ex6)


# EXERCICE 7 : Division avec résultat flottant
a = donnees["ex7_a"]
b = donnees["ex7_b"]
# Divisez a par b
resultat_ex7 = a / b
print(resultat_ex7)


# EXERCICE 8 : Calculer le reste d'une division
dividende = donnees["ex8_dividende"]
diviseur = donnees["ex8_diviseur"]
# Calculez le reste (modulo)
resultat_ex8 = dividende / diviseur
print(resultat_ex8)

# EXERCICE 9 : Conversion de types
# Age en tant que chaîne
age_str = donnees["ex9_age"]
# Convertissez en entier
age_int = int(age_str)
# Créez le message : "Vous avez [âge] ans."
resultat_ex9 = str(age_int)
print("Vous avez " + resultat_ex9 + " ans")

# EXERCICE 10 : Afficher le type d'une variable
valeur = donnees["ex10_valeur"]
# Utilisez type() pour obtenir le type
type_valeur = type(valeur)
# Créez un message : "Valeur: 3.14, Type: <class 'float'>"
resultat_ex10 = "Valeur : 3.14, Type : " + str(type_valeur)
print(resultat_ex10)

# EXERCICE 11 : Manipuler une chaîne
texte = donnees["ex11_texte"]
# Transformez en majuscules
resultat_ex11 = texte.upper();
print(resultat_ex11)

# EXERCICE 12 : Longueur d'une chaîne
phrase = donnees["ex12_phrase"]
# Calculez la longueur
resultat_ex12 = len(phrase)
print(resultat_ex12)


# EXERCICE 13 : Convertir des Celsius en Fahrenheit
# Formule : F = (9/5) * C + 32
celsius = donnees["ex13_celsius"]
# Calculez en Fahrenheit
resultat_ex13 = (9/5) * celsius + 32
print(resultat_ex13)

# EXERCICE 14 : Opérations arithmétiques
num1 = donnees["ex14_num1"]
num2 = donnees["ex14_num2"]
# Créez un dictionnaire avec :

# - "addition": résultat addition
resultat_ex14 = num1 + num2 
print(num1 , "+",  num2 ,"=", resultat_ex14)

# - "soustraction": résultat soustraction
resultat_ex14 = num1 + num2 
print(num1 , "+",  num2 ,"=", resultat_ex14)

# - "multiplication": résultat multiplication
resultat_ex14 = num1 * num2 
print(num1 , "*",  num2 ,"=", resultat_ex14)

# - "division": résultat division
resultat_ex14 = num1 / num2 
print(num1 , "/",  num2 ,"=", resultat_ex14)

# EXERCICE 15 : Écrire un commentaire
# Ce programme démontre les opérations de base en Python
# Calculez : (5 + 3) * 2
a = 5
b = 3
c = 2
# Résultat de (a + b) * c
resultat_ex15 = (a + b) * c
print(resultat_ex15)
