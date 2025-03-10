import sqlite3 as sgbd
from datetime import date, timedelta
class Usager:
    def __init__(self, code_barre):
        self.cnx= sgbd.connect('/home/tnsi-eleve5/mediatheque.db')
        self.c = self.cnx.cursor()
        self.code_barre = code_barre

    def __del__(self):
        self.cnx.close()

    def emprunter(self, isbn):
        self.c.execute('INSERT INTO emprunt VALUES (?,?,?)', [self.code_barre, isbn, date.today()+timedelta(days=30)])

    def rendre(self, isbn):
        self.c.execute('DELETE FROM emprunt WHERE isbn = ?', [isbn])
        
    def emprunts(self):
        self.c.execute('SELECT retour, titre, emprunt.isbn FROM emprunt JOIN livre ON emprunt.isbn = livre.isbn WHERE emprunt.code_barre = ?', [self.code_barre])
        return self.c.fetchall()

u = Usager("137332830764072")
print(u.emprunts())
u.rendre('978-2013230827')
u.emprunter('978-0132762564')
print(u.emprunts())