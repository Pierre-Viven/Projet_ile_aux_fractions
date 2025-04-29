from openpyxl import load_workbook as Charger_Tableur
from openpyxl import Workbook as Nouveau_Tableur
import socket
import os

def Remplir_Tableur(temps, tentatives, niveau, succes):
    # Charger le fichier Excel
    tableur = Charger_Tableur("data.xlsx")

    # Sélectionner une feuille
    feuille = tableur["F1"]

    #Recherche de la 1ère ligne vierge
    ligne = 1
    v = feuille["A"+str(ligne)].value
    while(v!=None):
        ligne += 1
        v = feuille["A"+str(ligne)].value
    

    #Remplissage de la ligne
    feuille["A"+str(ligne)].value = 1  #Si modification du jeu  à changer !!
    feuille["B"+str(ligne)].value = socket.gethostbyname(socket.gethostname())
    feuille["C"+str(ligne)].value = temps
    feuille["D"+str(ligne)].value = tentatives
    feuille["E"+str(ligne)].value = niveau
    feuille["F"+str(ligne)].value = succes


    # Sauvegarder les modifications
    tableur.save("data.xlsx")




def Creer_Tableur():
    if os.path.exists("data.xlsx"):
        os.remove("data.xlsx")
    # Créer un nouveau classeur
    tableur = Nouveau_Tableur()

    # Créer une feuille
    feuille = tableur.active
    feuille.title = "F1"

    #Remplier la première ligne
    feuille["A1"] = "Version"
    feuille["B1"] = "ID"
    feuille["C1"] = "Temps"
    feuille["D1"] = "Tentatives"
    feuille["E1"] = "Niveau"
    feuille["F1"] = "Succès"



    # Enregistrer le fichier
    tableur.save("data.xlsx")
