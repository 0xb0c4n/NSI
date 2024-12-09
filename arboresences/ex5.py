import xml.dom.minidom as dom

doc = dom.parse("test.xml")
def stat_xml(d):
    e = 0
    a = 0
    t = 0
    if d.attributes:
        a = len(d.attributes)
    elif d.nodeType == dom.Node.ELEMENT_NODE:
        e = 1
    elif d.nodeType == dom.Node.TEXT_NODE:
        t = 1

    for c in d.childNodes:
        te, ta, tt = stat_xml(c)
        e += te
        a += ta
        t += tt

    return e, a, t

print(stat_xml(doc))

