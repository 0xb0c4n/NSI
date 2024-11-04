class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def deplacer(self,dx,dy):
        self.x += dx
        self.y += dy

class Triangle:
    def __init__(self, p1,p2,p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def deplacer(self, dx, dy):
        self.p1.deplacer(dx,dy)
        self.p3.deplacer(dx,dy)
        self.p2.deplacer(dx,dy)

a = Point(1,1)
b = Point(3,5)
c = Point(-4,-6)
d = Point(7,-9)

t1 = Triangle(a,b,c)
t2 = Triangle(b,c,d)
