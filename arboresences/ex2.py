from strings import *
from ex1 import *
import os

def repertoires(r):
    dir = os.listdir(r)
    liste = []
    dir_name = r.split("/")[-1]
    for elt in dir:
        if os.path.isdir(os.path.join(r, elt)):
            liste.append(repertoires(os.path.join(r, elt)))
        else:
            liste.append(Noeud(elt, []))
    arbre = Noeud(dir_name, liste)
    return arbre

arbre = repertoires("/home/tnsi-eleve5/nsi")
print(affiche(arbre, 1))