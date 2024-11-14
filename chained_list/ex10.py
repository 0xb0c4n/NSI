from Cellule import *

def liste_tableau(t):
    cellule = None
    for i in range(0, len(t), -1):
        cellule = Cellule(t[i], cellule)
    return cellule