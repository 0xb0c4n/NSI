import sqlite3 as sgbd
import csv

bdd = sgbd.connect("/home/tnsi-eleve5/mediatheque.db")

c = bdd.cursor()
c.execute("SELECT * FROM usager")

with open("usager.csv", "w", encoding="utf-8") as f:
    s = csv.writer(f)
    s.writerow(['nom', 'prenom', 'adresse', 'cp', 'ville', 'email', 'code_barre'])
    for elt in c.fetchall():
        s.writerow(elt)