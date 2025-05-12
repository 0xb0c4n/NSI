from Graphe import *

def parcours_ch(g, vus, org, s):
	if s not in vus:
		vus[s] = org
		for v in g.voisins(s):
			parcours_ch(g, vus, s, v)

def chemin(g, u, v):
	vus = {}
	parcours_ch(g, vus, None, u)
	if v in vus:
		return True
	else:
		return None

