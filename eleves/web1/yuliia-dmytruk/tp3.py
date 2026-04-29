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
resultat_ex1 = list(mot)


# EXERCICE 2 : Compter une lettre
mot = donnees["ex2_mot"]
lettre = donnees["ex2_lettre"]
# Comptez combien de fois la lettre "a" apparaît
res=0
for c in mot:
    if c== lettre:
        res+=1
resultat_ex2 = res


# EXERCICE 3 : Compter les voyelles
mot = donnees["ex3_mot"]
# Comptez les voyelles (a, e, i, o, u, y)
vowels = "aeiouy"
resultat_ex3 = 0
i = 0
while i < len(mot):
  if mot[i] in vowels:
   resultat_ex3 = resultat_ex3 + 1
  i = i + 1
print(resultat_ex3)


# EXERCICE 4 : Inverser une chaîne
mot = donnees["ex4_mot"]
# Affichez le mot à l'envers : "hello" → "olleh"
reverse_word=""
for letter in mot:
    reverse_word=letter+reverse_word
resultat_ex4 = reverse_word


# EXERCICE 5 : Vérifier un palindrome
mot = donnees["ex5_mot"]
# Vérifiez si le mot se lit pareil dans les deux sens
# "radar" → True
reverse_word=""
for letter in mot:
   reverse_word=letter+reverse_word
if mot in reverse_word:
 resultat_ex5 = True 
else:
   resultat_ex5 = False 



# EXERCICE 6 : Compter les mots
phrase = donnees["ex6_phrase"]
# Comptez combien de mots la phrase contient (sans utiliser split)
res=1
for c in phrase:
    if c ==" ":
     res+=1
resultat_ex6 = res


# EXERCICE 7 : Supprimer les espaces en début et fin
phrase = donnees["ex7_phrase"]
# Retournez la phrase sans espaces au début et fin
resultat_ex7 = None


# EXERCICE 8 : Trouver le mot le plus long
phrase = donnees["ex8_phrase"]
# Retournez le mot le plus long de la phrase (sans utiliser split)
curr_word=""
biggest_word=0
for c in phrase:
    if c != " ":
        curr_word+=c
        
    else:
        if len(curr_word) > biggest_word:
            biggest_word= len(curr_word)
        curr_word = ""
        
resultat_ex8 = biggest_word


# EXERCICE 9 : Supprimer les espaces multiples
phrase = donnees["ex9_phrase"]
# Transformez "Bonjour  tout   le    monde" en "Bonjour tout le monde"
res = ""
last_char=""
for c in phrase:
    if c != " " or (last_char != " " and last_char != ""):
        res+= c
    last_char=c
if res != "" and res[-1] == " ":
    res = res[:-1]
resultat_ex9 = res

# EXERCICE 10 : Inverser les mots d'une phrase
phrase = donnees["ex10_phrase"]
# "Python est genial" → "genial est Python"
resultat_ex10 = None


# EXERCICE 11 : Supprimer les caractères consécutifs identiques
chaine = donnees["ex11_chaine"]
# "booonnjooour" → "bonjour"
resultat_ex11 = None


# EXERCICE 12 : Compression simple d'une chaîne
chaine = donnees["ex12_chaine"]
# "aaabbc" → "a3b2c1"
resultat_ex12 = None


# EXERCICE 13 : Vérifier des parenthèses équilibrées
expression = donnees["ex13_expression"]
# Vérifiez si les parenthèses sont correctement équilibrées
# "(a + b) * (c - d)" → True
resultat_ex13 = None


# EXERCICE 14 : Vérifier deux anagrammes
mot1 = donnees["ex14_mot1"]
mot2 = donnees["ex14_mot2"]
# Vérifiez si les deux mots sont des anagrammes
# "listen" et "silent" → True
count1={}
count2={}
if len(mot1) != len(mot2):
    resultat_ex14=False
else:
    for c in mot1:
        if c in count1:
            count1[c]+=1
        else:
         count1[c] = 1
    for c in mot2:
        if c in count2:
            count2[c]+=1
        else:
         count2[c] = 1
    if count1 == count2:
        resultat_ex14 = True
    else:
        resultat_ex14 = False


# EXERCICE 15 : Mini analyseur de phrase
phrase = donnees["ex15_phrase"]
# Retournez un dictionnaire avec :
# - "nombre_mots": nombre de mots
# - "mot_le_plus_long": le mot le plus long
# - "nombre_caracteres": nombre total de caractères (sans espaces)
resultat_ex15 = None
