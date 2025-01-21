def fusion(t, g, d, m):
    n1 = m - g + 1
    n2 = d - m
    lg = t[g:m+1]
    ld = t[m:d+1]
    for i in range(n1):
        lg[i] = t[g+i]
    for j in range(n2):
        ld[j] = t[m+1+j]

    lg[n1] = t[m]+1
    ld[n2] = t[d]+1
    i = 0
    j = 0
    for k in range(g, d+1):
        if lg[i] <= ld[j]:
            t[k] = lg[i]
            i += 1
        else:
            t[k] = ld[j]
            j += 1

def fusion2(t, g, m, d):
    n1 = m - g + 1
    n2 = d - m
    lg = t[g:m+1]
    ld = t[m:d+1]
    for i in range(n1):
        lg[i] = t[g+i]
    for j in range(n2):
        ld[j] = t[m+1+j]

    i = 0
    j = 0
