from Noeud import *
from ex4 import *

def parfait(h):
    if h == 0:
        return None
    else:
        return Noeud(parfait(h-1), 2**(h-1), parfait(h-1))
    
print(str_arbre(parfait(6)))
print(taille(parfait(6))==2**6 - 1)