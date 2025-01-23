def fusion(t, g, d, m):
    n1 = m - g + 1
    n2 = d - m
    lg = t[0:n1]
    ld = t[0:n2]
    print(lg, ld)
    for i in range(n1):
        lg[i] = t[g + i]
    for j in range(n2):
        ld[j] = t[m+1+j]

    lg.append(lg[-1]+1)
    ld.append(ld[-1]+1)

    i = 0
    j = 0

    for k in range(g, d+1):
        if lg[i] <= ld[j]:
            t[k] = lg[i]
            i += 1
        else:
            t[k] = ld[j]
            j +=1

def tri_fusion(t, g, d):
    if g < d:
        m = (g+d)//2
        print(m)
        tri_fusion(t, g, m)
        tri_fusion(t, m+1, d)
        fusion(t, g, d, m)

t = [5,2,15,85,69,43,4]
tri_fusion(t, 0, 7)
print(t)