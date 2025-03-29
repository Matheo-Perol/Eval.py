#Objectif trouver si une figure et symetrique 

import random

#---------------------------------------
#Question 1 

    #Cette fonction génère un tableau  'O' et 'X' de manière aléatoire.
def generer_tableauX(n, m):
    return [[random.choice("OX")  # Choisit aléatoirement 'O' ou 'X'
              for _ in range(m)]   # Remplir chaque ligne avec m 
                for _ in range(n)]  # Répète l'opération pour n 

def affiche_image_symetrie2(tab):

    for ligne in tab:  
        # Vérifie la symétrie sur chaque ligne en comparant chaque élément avec son opposé
        print(" ".join("O" if ligne[j] == ligne[9 - j] else "X" for j in range(10)))  # Affiche 'O' si la valeur est symétrique, sinon 'X'
#--------------------------------------------------------
#  Question 2 
#objectif:Génère un tableau aléatoire de dimensions n x m contenant des entiers entre 0 et 9.#


import random


def generer_tableau_denombre(n, m):

    return [[random.randint(0, 9) for _ in range(m)] for _ in range(n)]

# Fonction pour vérifier si chaque ligne du tableau est symétrique
def verif_symetrie(tab):
   #verrifie si tous ca est bien symetrique 
    for i in range(10):  #
        for j in range(5):  # Compare les éléments opposés jusqu'à la moitié de la ligne
            if tab[i][j] != tab[i][9 - j]:
                return False  # Retourne False si une asymétrie est détectée ou pas 
    return True  

# Fonction si il est  symétrique
def affiche_image(tab):
    #Affiche le tableau et dit si il  est symétrique ou non.#
    for ligne in tab:  # regarde  chaque ligne du tableau
        print(" ".join(map(str, ligne)))  # Affiche chaque ligne sous forme de chaîne de nombres
    # affiche du résultat de la symétrie
    print("Symétrique" 
          if verif_symetrie(tab) 
          else "Pas symétrique")


#----------------------------------------------------------------------------------------------------
#ca c est pour mettre la variable tab 

tab = generer_tableau_denombre(10, 10)# pour la question 2
affiche_image(tab)# pour la question 2

tab = generer_tableauX(10, 10)# pour la question 1 
affiche_image_symetrie2(tab)# pour la question 1


