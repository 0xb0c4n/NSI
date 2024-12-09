from strings import *

def affiche(a, i):
    string = str(a.valeur)
    for elt in a.fils:
        string += "\n" + " "*(i) + affiche(elt,i+1)
    return string
