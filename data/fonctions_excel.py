from openpyxl import load_workbook as Charger_Tableur
from openpyxl import Workbook as Nouveau_Tableur


def Remplir_Tableur(nom_Fichier, version, iD, temps, tentatives, erreurs):
    # Charger le fichier Excel
    tableur = Charger_Tableur(nom_Fichier+".xlsx")

    # Sélectionner une feuille
    feuille = tableur["F1"]

    #Recherche de la 1ère ligne vierge
    ligne = 1
    v = feuille["A"+str(ligne)].value
    while(v!=None):
        ligne += 1
        v = feuille["A"+str(ligne)].value
    

    #Remplissage de la ligne
    feuille["A"+str(ligne)].value = version
    feuille["B"+str(ligne)].value = iD
    feuille["C"+str(ligne)].value = temps
    feuille["D"+str(ligne)].value = tentatives
    feuille["E"+str(ligne)].value = erreurs


    # Sauvegarder les modifications
    tableur.save(nom_Fichier+".xlsx")




def Creer_Tableur(nom_Fichier):
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
    feuille["E1"] = "Erreurs"



    # Enregistrer le fichier
    tableur.save(nom_Fichier+".xlsx")
