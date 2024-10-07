from nsi.recursivity.ex5 import pgcd

class Fraction:
    def __init__(self, num, den):
        pgcdn = pgcd(num, den)
        self.num = num / pgcdn
        self.den = den /pgcd
        
        if self.den <= 0:
            raise ValueError
        
    def __str__(self):
        if(self.den) == 1:
            return str(self.num) 
        else:          
            return str(self.num) + " / " + str(self.den)
        
    def __eq__(self, j):
        if self.num * j.den == j.num * self.den:
            return True
        else: 
            return False

    def __lt__(self, j):
        if self.num * j.den < j.num * self.den:
            return True
        else: 
            return False
        
    def __add__(self, j):
        return Fraction(self.num * j.den + self.den* j.num, j.den * self.den)

    def __mul__(self, j):
        return Fraction(self.num * j.num, self.den * j.den)



# Jeu de tests
f1 = Fraction(5,3)
f2 = Fraction(1,5)

assert str(f1) == '5 / 3'
assert (f1 == f2)== False
assert f2 < f1 == True
assert f1 + f2 == Fraction(28,15)
assert f1 * f2 == Fraction(5,15)
assert f1._irreductible
