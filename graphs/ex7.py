class Noeud:
    def __init__(self,g,v,d):
        self.gauche = g
        self.valeur = v
        self.droite = d

def parfait(h):
    if h == 0:
        return None
    else:
        return Noeud(parfait(h-1), h, parfait(h-1))
	
arbre = parfait(5)

def largeur(a):
	dist = {a.valeur: 0}
	courant = {a}
	suivant = set()
	while len(courant) > 0:
		s = courant.pop()
		for v in [s.gauche, s.droite]:
			if v!= None and v.valeur not in dist:
				suivant.add(v)
				dist[v.valeur] = dist[s.valeur] + 1
		if len(courant) == 0:
			courant, suivant = suivant, set()
	return dist

def distance(g, u, v):
	dist = largeur(g, u)
	return dist[v] if v in dist else None


def str_arbre(a):
    if a is None:
        return ""
    else:
        return "(" + str_arbre(a.gauche) + str(a.valeur) + str_arbre(a.droite) + ")"

print(largeur(arbre))