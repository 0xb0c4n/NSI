euros = [1,2,5,10,20,50,100,200]
def monnaie(s):
    i = len(euros) - 1
    p = 0
    while s > 0:
        if s >= euros[i]:
            s -= euros[i]
            p += 1
        else:
            i -= 1
    return p

cur = None
for i in range(200):
    act = monnaie(i)
    if cur == None or act > cur:
        cur = i

print(cur)