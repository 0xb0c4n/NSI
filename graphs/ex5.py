from Graphe import *
def est_connexe(g):
	for sommet in g.sommets():
		tmp = [elt for elt in g.sommets if elt != sommet]
		for elt in tmp:
			if not(existe_chemin(g, sommet, elt)):
				return False
	return True


