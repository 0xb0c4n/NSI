class DbTab:
    def __init__(self, g, d):
        self.g = g[::-1]
        print(self.g)
        self.d = d

    def imin(self):
        return -len(self.g)+1
    
    def imax(self):
        return len(self.d)-1
    
    def append(self,elt):
        self.d.append(elt)

    def prepend(self, elt):
        if self.imin() <= 0:
            self.g.append(elt)[::-1]
        else:
            self.g.append(elt)

    def __getitem__(self, i):
        if i < 0:
            return self.g.reverse()[abs(i) - 1]
        else:
            return self.d[i]
        
    def __setitem__(self,elt,i):
        if i < 0:
            self.g.reverse()[abs(i) - 1] = elt
        else:
            self.d[i] = elt

    def __str__(self):
        return str(self.g[::-1] + self.d) 