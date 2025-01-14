from ex1 import *

lexique = ["Arbre", "Art", "Arbuste"]

def trouve(m, d):
    liste = []
    for mot in lexique:
        if hamming(mot, m) <= d:
            liste.append(mot)
    return liste

print(trouve("Arble", 3))