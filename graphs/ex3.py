from Graphe import *

assert distance(g, "Nouvelle Aquitaine", "Occitanie") > 0
assert distance(g, "Occitanie", "Occitanie") == 0
assert distance(g, "Occitanie", "Grand Est") == None
