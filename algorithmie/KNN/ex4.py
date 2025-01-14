def test(c, d):
    maxi = c if len(c) > len(d) else d
    for i in range(len(maxi)):
        copy = str(d)
        j = copy[:i] + copy[i+1:len(copy)]
        if c == j:
            return True
        
    return False

print(test("cnnard", "cannard"))