import Cellule

index = 0
def nieme_element(n, lst):
    while n > 0:
        if lst is None:
            raise ValueError 
        else:
            lst = lst.suivante
            n -= 1
            
    return lst.valeur