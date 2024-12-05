from strings import *

def affiche(a, i):
    string = str(a.valeur)
    for elt in a.fils:
        string += "\n" + " "*(i) + affiche(elt,i+1)
    return string

a = Noeud("A", [
    Noeud("B", [
        Noeud("D", [])
    ]),
    Noeud("C", [
        Noeud("E", []),
        Noeud("F", [
            Noeud("H", [])
        ]),
        Noeud("G", [])
    ])
])

print(affiche(a, 1))