def calcule(op,f,t):
	v = t[0]
	for i in range(1, len(t)):
		v = op(v, f(t[i])

	return str(v)[1:-1]