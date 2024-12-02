def minimum(a):
    if a is None:
        return None
    elif a.gauche is None:
        return a.valeur
    else:
        return minimum(a.gauche)
    
def supp(self, x):
    if self.racine.valeur > x:
        return self.supp(self.racine.gauche, x)
    elif self.racine.valeur < x:
        return self.supp(self.racine.droite, x)
    else:
        return Noeud()