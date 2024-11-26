from Noeud import *

def str_arbre(a):
    if a is None:
        return ""
    else:
        return "(" + str_arbre(a.gauche) + str(a.valeur) + str_arbre(a.droite) + ")"
