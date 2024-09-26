def cree():
    return [0] * 6

def contient(s,x):
    iEntier = x // 64
    bit = x % 64
    return (s[iEntier] & (1 << bit) != 0)

def ajoute(s,x):
    iEntier = x // 64
    bit = x % 64
    s[iEntier] = s[iEntier] | 1 << bit

def enumere(s):
    tab = []
    for date in s: 
        if bin(date) != 0:
            tab.append(date)
    return tab

def union(s1,s2):
    result = s1
    for elt2 in s2:
        if elt2 not in s1:
            result.append(elt2)

    return result

def inter(s1,s2):
    result = []
    for elt in s1:
        for elt2 in s2:
            if elt in s2 and elt not in result:
                result.append(elt)
    
    return result

def tranche(t,i,j):
    if j <= i:
        return []
    else:
        return [t[k] for k in range(i,j)]
    
def concatenation(t1,t2):
    return sorted(union(t1,t2))

def cree():
    return {}

def cle(d,k):
    return k in d

def lit(d,k):
    return d[k] if cle(d,k) else None

def ecrit(d,k,v):
    d[k] = v
    print(d)