def bin_packaging(c,n,tab):
    n_dict = {i: 0 for i in range(1,n+1)}
    for elt in tab:
        for p in n_dict:
            if c - n_dict[p] >=  elt:
                n_dict[p] += elt
            elif n == p:
                print(p)
                return False
    return True

print(bin_packaging(10, 3, [6,3,1, 10, 6, 4]))