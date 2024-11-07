

#Recursive

def trouve(x, lst):
    if lst is None:
        return None 
    elif x == lst.valeur:
        return 0
    else:
        trouver = trouve(x, lst.suivante)
        if trouver is None:
            return None
        else:
            return 1+trouve(x, lst.suivante)

#While

def trouve_while(x, lst):
    i = 0
    while lst is not None:
        if x == lst.valeur:
            return i
        i += 1
    return None