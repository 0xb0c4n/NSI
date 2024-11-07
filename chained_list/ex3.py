import Cellule

#Recursive
def occurences(x, lst):
    if lst is None:
        return 0
    else:
        return 1 + occurences(x, lst.suivante) if x == lst.val else occurences(x, lst.suivante)

#While
def occurences_while(x, lst):
    i = 0
    while lst != None:
        if x == lst.valeur:
            i+=1
        lst = lst.suivante
    return i