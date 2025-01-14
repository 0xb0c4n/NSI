from ex1 import *

lexique = ["Arbre", "Art", "Arbuste"]

def trouve_min(lexique, m):
    mot_min = lexique[0]
    for mot in lexique:
        if hamming(m, mot_min) > hamming(m, mot):
            mot_min = mot

    return mot_min

print(trouve_min(lexique, "Arabe"))