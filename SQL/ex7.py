import xml
import sqlite3 as sgbd

bdd = sgbd.connect("/home/tnsi-eleve5/mediatheque.db")

a1 = input("Entrez une année de départ : ")
a2 = input("Entrez une année de fin :")

c = bdd.cursor()
c.execute("SELECT * FROM livre WHERE annee <= ? AND annee >= ?", [max(a1, a2), min(a1, a2)])

html_s = "<html><body><table><thead><tr><th>Titre</th><th>Edition</th><th>Année</th><th>Code barre</th></tr></thead><tbody>"

for elt in c.fetchall():
    html_s += "<tr><td>" + str(elt[0]) + "</td><td>" + elt[1] + "</td><td>" + elt[2] + "</td><td>" + elt[3] + "</td></tr>"

html_s += "</tbody></table></body></html>"

with open("index.html", "a") as f:
    f.write(html_s)