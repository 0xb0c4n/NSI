import xml.dom.minidom as dom

doc = dom.parse("test.xml")

def compte_balise(d, n):
    i = 0
    if d.nodeName == n:
        i = 1
        
    for c in d.childNodes:
        i += compte_balise(c, n)

    return i

print(compte_balise(doc, "calories"))