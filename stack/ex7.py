class FileBornée:
    def __init__(self, c):
        self._tab = [None]*c
        self._nb = 0
        self.premier = 0

    def est_vide(self):
        return self._nb == 0
    
    def est_pleine(self):
        return self._nb == len(self._tab)
    
    def ajouter(self, e):
        if self.est_pleine():
            raise IndexError("La liste est pleine")
        else:
            self._tab[(self.premier+self._nb)%len(self._tab)] = e
            self._nb+=1

    def retirer(self):
        if self.est_vide():
            raise IndexError("La liste est vide")
        else:
            elt = self._tab[self.premier]
            self._tab[self.premier] = None
            self.premier+=1
            return elt  
        
    def __str__(self):
        return str(self._tab)
    
def creer_file(c):
    return FileBornée(c)
