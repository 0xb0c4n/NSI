from Pile import *

class File:
    def __init__(self):
        self._entree = creer_pile()
        self._sortie = creer_pile()

    def est_vide(self):
        return self._entree.est_vide() and self._sortie.est_vide()
    
    def ajouter(self, e):
        self._entree.empiler(e)

    def retirer(self):
        if self._sortie.est_vide():
            while not self._entree.est_vide():
                self._sortie.empiler(self._entree.depiler())
        if self._sortie.est_vide():
            raise IndexError("retire sur une file vide")
        return self._sortie.depiler()
    
def creer_file():
    return File()