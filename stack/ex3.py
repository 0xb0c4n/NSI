from Pile import *
from File import *

def parenthese_ferme(string, index):
    p = creer_file()
    for i in range(len(string)):
        if index >= len(string):
            return None
        elif i == index:
            precedent = p.retirer()
            if precedent['char'] == '(':
                return precedent['index']
            else:
                return None
        else:
            if string[i] in '()':
                p.ajouter({"char": string[i], "index": i})

print(parenthese_ferme("zet(gtrt()())0",9))
print(parenthese_ferme("zet(gtrt()())0",2))