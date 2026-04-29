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

resultat_ex1 = list(mot)


# EXERCICE 2 : Position des caractères
# Affichez chaque lettre du mot "programmation" avec sa position
# Exemple résultat : "p:0 r:1 o:2 g:3..." (comme string ou dict)
mot = donnees["ex2_mot"]
resultat_ex2 = {}
for i in range(len(mot)):
    resultat_ex2[i] = mot[i]
  



# EXERCICE 3 : Codes des caractères
# Retournez le code ASCII d'un caractère avec ord()
char = donnees["ex3_char"]
# Code ASCII de "A"
resultat_ex3 = ord(char)


# EXERCICE 4 : Majuscule ou minuscule
# Utilisez le code ASCII pour déterminer si c'est majuscule ou minuscule
lettre = donnees["ex4_lettre"]
# Retournez "majuscule" ou "minuscule"

if ord(lettre)>=ord("a") and ord(lettre)<= ord("z"):
      resultat_ex4 = "minuscule"
elif  ord(lettre)>=ord("A") and ord(lettre)<= ord("Z"):
      resultat_ex4 = "majuscule"


# EXERCICE 5 : Est-ce un chiffre ?
# Utilisez le code ASCII pour vérifier si c'est un chiffre
char = donnees["ex5_char"]
# Retournez True ou False

if ord(char)>=ord("0") and ord(char)<=ord("9"):
    resultat_ex5 = True
else: resultat_ex5= False


# EXERCICE 6 : Compter les chiffres dans un texte
phrase = donnees["ex6_phrase"]
# Comptez combien de chiffres (0-9) la phrase contient
# Indice : ord('0') = 48, ord('9') = 57
count=0
for i in phrase:
     if i>="0" and i<="9":
          count+=1
resultat_ex6 = count


# EXERCICE 7 : Somme des chiffres d'un texte
chiffres_text = donnees["ex7_chiffres"]
# Convertissez chaque caractère chiffre en nombre et additionnez
# "1352" → 1 + 3 + 5 + 2 = 11
sum=0
for i in chiffres_text:
     sum=sum+ord(i)-ord("0")
resultat_ex7 = sum


# EXERCICE 8 : Construire un nombre
# Lisez un nombre texte caractère par caractère
# Utilisez la formule : resultat = resultat * 10 + chiffre
nombre_text = donnees["ex8_nombre_text"]
# Convertissez "42" en nombre 42 (sans utiliser int())
to_number=0
for i in nombre_text:
     to_number=to_number*10+ord(i)-ord("0")
resultat_ex8 = to_number


# EXERCICE 9 : Vérifier une entrée numérique
texte = donnees["ex9_texte"]
# Vérifiez si le texte ne contient QUE des chiffres
# "123abc456" → False (contient des lettres)
# "123456" → True
resultat_ex9=True
for i in texte:
    if ord(i) >= ord("a") and ord(i) <= ord("z") or ord(i) >= ord("A") and ord(i) <= ord("Z"):
      resultat_ex9 = False




# EXERCICE 10 : Mini addition de nombres texte
num1_text = str(donnees["ex10_num1"])  # "12"
num2_text = str(donnees["ex10_num2"])  # "3"
# Convertissez manuellement en nombres (sans int())
# puis additionnez et retournez le résultat
to_num1=0
to_num2=0
for i in num1_text:
     to_num1=to_num1*10+(ord(i)-ord("0"))
for i in num2_text:
     to_num2=to_num2*10+(ord(i)-ord("0"))
resultat_ex10 = to_num1+to_num2


# EXERCICE 11 : Extraire les chiffres d'un nombre
nombre = donnees["ex11_nombre"]
# Affichez les chiffres un par un en utilisant % et //
# 1234 → ['1', '2', '3', '4'] ou "1234"
digit = ""
while nombre >0:
     last_digit=nombre%10
     digit=f"{last_digit}"+digit
     nombre=nombre//10
resultat_ex11=digit


# EXERCICE 12 : Inverser un nombre
nombre = donnees["ex12_nombre"]
# Affichez le nombre avec chiffres inversés
# 5678 → 8765
reverse_num=0
while nombre >0:
     last_digit=nombre%10
     reverse_num=reverse_num*10+last_digit
     nombre=nombre//10
resultat_ex12=reverse_num



# EXERCICE 13 : Bonus - Calculatrice simple
expression = donnees["ex13_expression"]
# Parsez une expression comme "12+3"
# Identifiez les nombres et l'opérateur
# Retournez le résultat du calcul
# "12+3" → 15
num1=0
num2=0
sign=""

for i in expression:
     if ord(i)>=ord("0") and ord(i)<=ord("9"):
          digit=ord(i) - ord("0")
          if sign == "":
            num1 = num1 * 10 + digit 
          else:
            num2 = num2 * 10 + digit 
     elif i == "+" or i == "-" or i == "*" or i == "/":
            sign = i
        
     
if sign=="+":
          resultat_ex13=num1+num2
elif sign=="-":
          resultat_ex13=num1-num2
elif sign=="*":
          resultat_ex13 =num1*num2
else:
          resultat_ex13=num1/num2

