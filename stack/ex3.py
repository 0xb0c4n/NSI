from Pile import *

operateurs = ["*", "+"]
def inverse_polonais(string):
    pile = creer_pile()
    tab = string.split()
    for letter in tab:
        if letter in operateurs:
            op1 = pile.depiler()
            op2 = pile.depiler()
            result = op1 + op2 if letter == "+" else op1*op2
            pile.empiler(result)
        else:
            try:
                pile.empiler(int(letter))
            except:
                pass
    if len(pile) != 1:
        return None
    else:
        return pile.depiler()
    
print(inverse_polonais("1 2 3 * + 4 *"))
print(inverse_polonais("1 2 3 + 4 *"))
print(inverse_polonais("1 2 3 * + 4"))
print(inverse_polonais(""))
print(inverse_polonais("a"))
