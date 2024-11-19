from Pile import *


def check_format(string):
    pile = creer_pile()
    dico = {"(": ")", "[": "]"}

    for letter in string:
        if letter in '([':
            pile.empiler(letter)
        elif letter in ')]':
            pr = pile.depiler()
            if dico[pr] != letter:
                return False
    return True

print(check_format("retr([])"))
print(check_format("retr([)]"))
print(check_format("retr(][)"))