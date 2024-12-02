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


def ajoute(a, e):
        if a is None:
            return Noeud(None, e, None)
        elif a.valeur > e:
            return Noeud(ajoute(a.gauche, e), a.valeur, a.droite)
        else:
            return Noeud(a.gauche, a.valeur, ajoute(a.droite, e))
    
test = Noeud(None, 15, None)
ajoute(test, 5)
print(str_arbre(test))