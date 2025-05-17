from openpyxl import load_workbook as Charger_Tableur
from openpyxl import Workbook as Nouveau_Tableur
import socket
import os
import sys


def chemin_exe(chemin_relatif):
    """Permet d'accéder aux fichiers même après compilation avec PyInstaller"""
    try:
        repertoire = sys._MEIPASS  # PyInstaller crée un répertoire temporaire
    except Exception:
        repertoire = os.path.abspath(".")
    return os.path.join(repertoire, chemin_relatif)



def Remplir_Tableur(temps, tentatives, niveau, succes):
    # Charger le fichier Excel
    chemin = chemin_exe("data.xlsx")
    tableur = Charger_Tableur(chemin)

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
    tableur.save(chemin)




def Creer_Tableur():
    chemin = chemin_exe("data.xlsx")
    if os.path.exists(chemin):
        os.remove(chemin)
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
    tableur.save(chemin)
