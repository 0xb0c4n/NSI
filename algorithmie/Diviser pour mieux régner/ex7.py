def deplacer(a,b,c,k):
    if k == 1:
        print(f"deplace {k} vers {c}")
    else:
        deplacer(a,b,c,k-1)

def hanoi(n):
    deplacer(1,2,3,n)

hanoi(5)
