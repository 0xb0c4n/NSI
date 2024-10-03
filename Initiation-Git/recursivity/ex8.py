import turtle
t= turtle.Pen()

def koch(n,l):
	if n == 0:
		t.forward(l)
	else:
		koch(n-1, l/3)
		t.left(60)
		koch(n-1, l/3) 
		t.right(120)		
		koch(n-1, l/3)
		t.left(60)
		koch(n-1, l/3)

koch(50,10)
