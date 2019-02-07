# -*- coding: utf-8 -*-


# version brute perso

annee = input("Saisissez une année : ")
annee = int(annee)

if annee%4 != 0:
    print ("Ce n'est pas une année bissextile")
elif annee%400 == 0:
    print("C'est une année bissextile")
elif annee%100 == 0:
    print("Ce n'est pas une année bissextile")
else:
    print ("C'est une année bissextile")


    
# version optim

annee = input("Saisissez une année : ")
try: # On essaye de convertir l'année en entier
    annee = int(annee)
except:
    print("Erreur lors de la conversion de l'année.")

if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    print("C'est une année bissextile.")
else:
    print("Ce n'est pas une année bissextile.")
    
    
    
    
    
    
# passage en fonction

def bissextile():
    annee = input("Saisissez une année : ")
    try: # On essaye de convertir l'année en entier
        annee = int(annee)
    except:
        print("Erreur lors de la conversion de l'année.")

    if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
        print("C'est une année bissextile.")
    else:
        print("Ce n'est pas une année bissextile.")
    

bissextile()