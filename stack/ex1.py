from Pile import *

class Historique:
    def __init__(self):
        self.addresse_courante = None
        self._addresses_precedentes = creer_pile()
        self.addresses_suivantes = creer_pile()

    def aller_a(self, addr):
        if not self.addresse_courante is None:
            self._addresses_precedentes.empiler(self.addresse_courante)
        self.addresse_courante = addr

    def retour(self):
        if not self._addresses_precedentes.est_vide():
            self.addresse_courante = self._addresses_precedentes.depiler()
        else:
            self.addresse_courante = None
            
    def retour_avant(self):
        if not self.addresses_suivantes.est_vide():
            self.addresse_courante = self.addresses_suivantes.depiler()

# ****************** TESTS ******************
h = Historique()
assert h.adresse_courante is None
h.aller_a("www.stackoverflow.com")
assert h.adresse_courante == "www.stackoverflow.com"
h.aller_a("www.developper.com")
h.retour()
assert h.adresse_courante == "www.stackoverflow.com"
h.aller_a("www.w3schools.com")
h.aller_a("openclassroom.com")
h.retour()
assert h.adresse_courante == "www.w3schools.com"
h.retour()
assert h.adresse_courante == "www.stackoverflow.com"
# on teste "retour" lorsqu'il n'y plus d'adresse antérieure
h.retour()
assert h.adresse_courante is None
#jeux de tests retour avant
h.retour_avant()
assert h.addresse_courante == "www.stackoverflow.com"
h.retour()
assert h.addresse_courante is None

h.aller_a("www.github.com")
assert h.addresses_suivantes is None

h.aller_a("www.stackoverflow.com") 
assert 