from Cellule import *
import sys

def inserer(x, lst):
    if lst is None:
        return Cellule(lst, x)
    else:
        if x < lst.valeur:
            return Cellule(x, lst)
        else:
            return inserer(x, lst.suivante)

def str_c(lst):
    if lst is None:
        return 

def tri_par_insertion(lst):
    if lst is None:
        return lst
    else:
        inserer(lst.valeur, lst)
        return tri_par_insertion(lst.suivante)
    
print(tri_par_insertion(Cellule(1,Cellule(5,Cellule(4,None)))))