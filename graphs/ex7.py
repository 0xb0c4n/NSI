def largeur(a, s):
	dist = {s: 0}
	courant = {s}
	suivant = set()
	while len(courant) > 0:
		s = courant.pop()
		for v in [a.gauche, a.droite]:
