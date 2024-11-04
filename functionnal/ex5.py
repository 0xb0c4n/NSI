import module

a = points(2,3)
b = points(1,5)
c = points(-5,6)
d = points(4,-4)

def deplacer_triangle(t,dx,dy):
   	empty = list(t)
	for elt in t:
		empty.append(deplacer(t,dx,dy))
	return triangle(tuple(empty))
	
t1 = triangle(a,b,c)
t2 = triangle(b,c,d)

t3 = deplacer_triangle(t1, -1,1)
t4 = deplacer_triangle(t2, 2, 3)
