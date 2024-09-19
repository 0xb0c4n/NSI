def coef(n,p):
	if p == 0 or n==p:
		return 1
	else:
		return coef(n-1,p-1)+coef(n-1,p)

triangle = []
for i in range(10):
	ligne = []
	for j in range(i):
		ligne.append(coef(i,j))
	ligne.append(1)
	triangle.append(ligne)

for elt in triangle:
	print(elt)
