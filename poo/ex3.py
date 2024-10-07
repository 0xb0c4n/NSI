class Intervalle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def est_vide(self):
        return self.b < self.a

    def __len__(self):
        return 0 if self.est_vide() else self.b - self.a
    
    def __contains__(self, x):
        return self.a <= x <= self.b

    def __eq__(self, i2):
        return self.est_vide() and i2.est_vide() or self.a == i2.a and self.b == i2.b 
    
    def __le__(self, i2):
        return i2.est_vide() and self.est_vide() or self.a >= i2.a and self.b <= i2.b
    
    def intersection(self, i2):
        if i2.a <= self.b and i2.a >= self.a:
            return Intervalle(i2.a, self.b)
        elif self <= i2:
            return Intervalle(i2.a,i2.b)
        elif self == i2:
            return Intervalle(self.a, self.b)
        else:
            return Intervalle(i2.b, self.a)
        
    def union(self, i2):
        if not i2.est_vide() and not self.est_vide():
            return Intervalle(min(self.a, i2.a), max(self.b, i2.b))
        else:
            return Intervalle(1,0)            
    
    