from math import sqrt
import csv
import os

### config ##

dataRepo = "/home/tnsi-eleve5/NSI/Initiation-Git"
dataFile = "iris.csv"
get_nom = {'0' : 'setosa', '1' : 'virginica', '2' : 'versicolor'}

def readCSV(dossier:str, fichier:str) -> list :
    """
    Entrée : le nom d'un fichier CSV (str)
    Sortie :  une liste de dictionnaires contenant les enregistrements
    """
    fic = os.path.join(dossier, fichier)
    with open(fic, mode = "r" , newline = '' , encoding='utf-8') as csvFile :
        reader = csv.DictReader(csvFile)
        lignes = [dict(ligne) for ligne in reader]
    return lignes

def distance(x1:float, y1:float, x2:float, y2:float) -> float:
    """
    renvoi la distance euclidienne entre (x1,y1) et (x2,y2)
    """
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def aj_distance(new_x:float, new_y:float, data:list) -> None:
    """
    Ajoute à 'data' une colonne 'distance' indiquant pour chaque ligne
    sa distance au nouveau point (new_x, new_y)
    """
    for dic in data:
        dic['distance']=distance(new_x, new_y, float(dic['petal_length']), float(dic['petal_width']))


def trier(data:list, cle:str) -> None:
    """
    tri par insertion de 'data' en fonction de la colonne 'cle'
    """
    for i in range(1, len(data)):
        j = i - 1
        a_trier = data[i][cle]
        while j >= 0 and data[j][cle] > a_trier:
            data[j+1] = data[j]
            j -= 1
        data[j+1][cle] = a_trier


def min(lst:list) -> int:
    """
    renvoi la position du plus petit élément de la liste
    """
    idx = 0
    mini = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < mini:
            idx = i
            mini = lst[i]

def knn(new_x, new_y, k):
    fleurs = readCSV(dataRepo, dataFile)
    aj_distance(new_x, new_y, fleurs)
    trier(fleurs,'distance')
    voisins = fleurs[:k]

    count = {"0" : 0, "1" : 0, "2" : 0} #cle 0 pour setosa etc ...
    espece_max = ''
    maximum = 0

    for fleur in voisins:
        count[fleur['species']] += 1
        if count[fleur['species']] > maximum:
            espece_max = get_nom[fleur['species']]
            maximum = count[fleur['species']]
    return espece_max, maximum



def main(new_x, new_y, k):
    print("\nAlgorithme des", k, "plus proches voisins.\n")

    espece, nb = knn(new_x, new_y, k)

    print("Le label le plus représenté est", espece)
    print("Il a atteint ", nb, "occurences sur les ", k, "possibles")

main(1.5,0.6,5)
