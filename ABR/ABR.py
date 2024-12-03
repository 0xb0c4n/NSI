import random

class Noeud:
    def __init__(self,g,v,d):
        self.gauche = g
        self.valeur = v
        self.droite = d


def str_arbre(a):
    if a is None:
        return ""
    else:
        return "(" + str_arbre(a.gauche) + str(a.valeur) + str_arbre(a.droite) + ")"


def ajouter(a, e):
    if a is None:
        return Noeud(None, e, None)
    elif a.valeur > e:
        return Noeud(ajouter(a.gauche, e), a.valeur, a.droite)
    else:
        if a.valeur != e:
            return Noeud(a.gauche, a.valeur, ajouter(a.droite, e))
        else:
            return a
            
def remplir(a, t):
    if a is None:
        return None
    remplir(a.gauche, t)
    t.append(a.valeur)
    remplir(a.droite, t)

class ABR:
    def __init__(self):
        self.racine = None

    def ajoute(self, e):
        self.racine = ajouter(self.racine, e)

    def lister(self):
        t = []
        remplir(self.racine, t)
        return t
    
    def __str__(self):
        return str_arbre(self.racine)
    
    
def trier(t):
    a = ABR()
    melange(t)
    for elt in t:
        a.ajoute(elt)
    return a.lister()

def melange(t):
    for i in range(len(t)):
        ri = random.randint(0, i)
        t[i], t[ri] = t[ri], t[i]
    

tri = trier([1,5,3,4,2,6,78])
print(tri)
