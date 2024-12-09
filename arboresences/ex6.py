import xml.dom.minidom as dom

def gen_doc(n):
    doc = dom.parseString('<a></a>')
    for i in range(n):
        b = doc.createElement('b')
        a = doc.childNodes[0]
        text = doc.createTextNode(str(i))
        b.appendChild(text)
        a.appendChild(b)
    print(type(doc))
    
    with open("docn.xml", mode="w", encoding="utf8") as f:
        f.write(doc.toxml())

gen_doc(8)