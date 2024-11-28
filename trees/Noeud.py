class Noeud:
    def __init__(self,g,v,d):
        self.gauche = g
        self.valeur = v
        self.droite = d

    def __eq__(self, n2):
        if n2 is None:
            return True
        else:
            return self.gauche == n2.gauche and self.valeur == n2.valeur and self.droite == self.droite
        
def taille(a):
    if a is None:
        return 0
    else:
        return 1 + taille(a.gauche) + taille(a.droite)
    
def hauteur(a):
    if a is None:
        return 0
    else:
        return 1 + max(hauteur(a.gauche), hauteur(a.droite))
    
