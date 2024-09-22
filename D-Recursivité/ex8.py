import turtle
t= turtle.Pen()

def koch(n,l):
	if n == 0:
		t.forward(l)
	else:
		koch(n-1, l)
		t.left(60)
		koch(n-1, l)
		t.right(120)		
		koch(n-1, l)
		t.left(60)
		koch(n-1, l)

koch(50,10)