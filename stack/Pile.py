class Cellule:
    def __init__(self, v, s):
        self.valeur = v
        self.suivante = s
    

class Pile:
    def __init__(self):
        self._contenu = None

    def est_vide(self):
        return self._contenu is None
    
    def empiler(self, e):
        self._contenu = Cellule(e, self._contenu)
    
    def __len__(self):
        v = longueur(self._contenu)
        return v

    def depiler(self):
        if self.est_vide():
            raise IndexError("depile une pile vide")
        v = self._contenu.valeur
        self._contenu = self._contenu.suivante
        return v

def longueur(contenu):
    if contenu is None:
        return 0
    else:
        return 1 + longueur(contenu.suivante)
    
def creer_pile():
    return Pile()