def nbChiffres(n):
	i = 1
	if n<10:
		return i
	return 1+nbChiffres(n/10)
