#Reproduire le pseudo code Mystere 
#Ajoute une fonction aleatoire 
#Fonction qui permet de savoir le nombre d achat pour 

def mystere(collection):
    res = True  
    for i in range(1, 11):  
        if collection[i] == 0:
            res = False  

    return res


#--------------------------------------------------------------------------
#Question 2

import random

# Fonction qui ajoute un nombre aléatoire entre 0 et 9 à la collection
def ajout(collection):
    collection.append(random.randint(0, 9)) # le .append sert a ajouter un element  a la fin d une liste 

# Fonction mystere
def mystere(collection):
    for i in range(len(collection)):  # Parcourt tous les éléments de la collection et les calcules
        if collection[i] == 0:  # Si un élément est égal à 0
            return False  
    return True  # Si aucun 0, retourne True

#--------------------------------------------------------------------------------------------------------------
#Question 3

import random

def test():
    tirages = 0
    chiffres_trouves = []
    while len(chiffres_trouves) < 10:
        nombre = random.randint(0, 9)
        if nombre not in chiffres_trouves: #not
            chiffres_trouves.append(nombre)
        tirages += 1
    print(tirages)

    #-------------------------------------------------------------------


    
collection = []
for _ in range(9):  
    ajout(collection)
print("Collection après ajouts :", collection)
resultat_mystere = mystere(collection)

test()