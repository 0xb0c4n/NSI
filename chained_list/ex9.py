from Cellule import *

def listeN(n):
    cellule = None
    for i in range(1, n+1, -1):
        cellule = Cellule(i, cellule)
        n-= 1
    return cellule