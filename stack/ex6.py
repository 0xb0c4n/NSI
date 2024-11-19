class PileBornée:
    def __init__(self, c):
        self._tab = [None]*c
        self._nb = 0
        
    def est_vide(self):
        for elt in self._tab:
            if elt != None:
                return False
        return True
        
    def est_pleine(self):
        for elt in self._tab:
            if elt == None:
                return False
        return True
    
    def empiler(self, e):
        if self.est_pleine():
            raise IndexError("La liste est pleine")
        else:
            self._tab[self._nb] = e
            self._nb+=1

    def depiler(self):
        if self.est_vide():
            raise IndexError("La liste est vide")
        else:
            self._nb-=1
            elt = self._tab[self._nb]
            self._tab[self._nb] = None
            return elt
        
    def __str__(self):
        return str(self._tab)
        
def creer_pile(c):
    return PileBornée(c)