def identiques(l1,l2):
    if l1 is None and l2 is None:
        return True
    elif l1.valeur == l2.valeur:
        return identiques(l1.suivante, l2.suivante)
    else:
        return False