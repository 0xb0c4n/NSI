import csv
import os
import math
import matplotlib.pyplot as plt

def valide(ligne):
    return {key: float(ligne[key]) for key in ligne}

def readCSV(rep: str, fic: str) -> list:
    fic = os.path.join(rep, fic)
    with open(fic, mode="r", newline="", encoding="utf-8") as f:
        reader = list(csv.DictReader(f))
        lignes = [valide(ligne) for ligne in reader]
    return lignes

def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

def aj_distance(new_x: float, new_y:float, data:list) -> None:
    for ligne in data:
        ligne["distance"] = distance(ligne["petal_length"], new_x, ligne["petal_width"], new_y)

def trier(data:list, cle:str) -> None:
    for i in range(1, len(data)):
        j = i
        while j > 0 and data[j-1][cle] > data[i][cle]:
            data[j] = data[j-1]
            j -= 1
        data[j] = data[i]

fleurs = readCSV("", "iris.csv")

#Affichage

def affichage(data:list) -> None:
    x1 = [ligne["petal_length"] for ligne in data if ligne["species"] == 0]
    x2 = [ligne["petal_length"] for ligne in data if ligne["species"] == 1]
    x3 = [ligne["petal_length"] for ligne in data if ligne["species"] == 2]
    plt.xlabel("Longueur de pétale")
    plt.ylabel("Largeur de pétale")
    plt.title("Nuages de points de pétales d'iris")

    y1 = [ligne["petal_width"] for ligne in data if ligne["species"] == 0]
    y2 = [ligne["petal_width"] for ligne in data if ligne["species"] == 1]
    y3 = [ligne["petal_width"] for ligne in data if ligne["species"] == 2]
    plt.scatter(x1, y1, c="red")
    plt.scatter(x2, y2, c="yellow")
    plt.scatter(x3, y3, c="green")
    plt.show()

#KNN

def knn(new_x:float, new_y:float, data:list, k:int):
    aj_distance(new_x, new_y, data)
    trier(data, "distance")
    species = [data[i]["species"] for i in range(k)]
    def count(da:list)->dict:
        dico = {0: 0, 1: 0, 2: 0}
        for elt in species:
            dico[elt]+=1
        return dico
    dico = count(species)
    return max(dico.values())

print(knn(1,2,fleurs,2))