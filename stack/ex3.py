from Pile import *

def parenthese_ferme(string, index):
    p = creer_pile()
    for i in range(len(string)):
        if index >= len(string):
            return None
        elif i == index:
            precedent = p.depiler()
            if precedent:
                return precedent
            else:
                return None
        else:
            if string[i] in '()':
                p.empiler(i)

print(parenthese_ferme("zet(gtrt()())0",9))
print(parenthese_ferme("zet(gtrt()())0",2))