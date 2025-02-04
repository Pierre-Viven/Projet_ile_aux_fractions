import pygame
import sys
from memory import Memory
from data.fonctions_excel import *

import time

pygame.init()


# Infos ecran
infoEcran = pygame.display.Info()
largeurEcran = infoEcran.current_w
hauteurEcran = infoEcran.current_h

# Configuration de l'affichage
ecran = pygame.display.set_mode((largeurEcran, hauteurEcran), pygame.SCALED | pygame.RESIZABLE)
pygame.display.set_caption("Îles aux fractions Memory")




#Images
imageAccueil = pygame.image.load("images/fond_ecran.jpg")  
imageAccueil = pygame.transform.scale(imageAccueil, (largeurEcran, hauteurEcran))




# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
gris = (100, 100, 100)
bleue = (0, 122, 204)
vert = (0, 204, 0)
rouge = (204, 0, 0)
jaune = (184,134,11)

# Police
policeTitre = pygame.font.SysFont('avenir', hauteurEcran // 10)
policeBase = pygame.font.SysFont('avenir', hauteurEcran // 20)



# Variables globales
pieces = 23  # Argent initial du joueur
niveaux = [True, False, False]   




# Fonction pour dessiner un bouton
def bouton_texte(texte, x, y, largeur, hauteur, couleur, couleurTexte, radius=200):
    pygame.draw.rect(ecran, couleur, (x, y, largeur, hauteur), border_radius=radius)
    label = policeBase.render(texte, True, couleurTexte)
    label_rect = label.get_rect(center=(x + largeur // 2, y + hauteur // 2))
    ecran.blit(label, label_rect)
    return pygame.Rect(x, y, largeur, hauteur)










# Page d'accueil
def menu():
    pygame.mixer.init() 
    pygame.mixer.music.load("son/musique_accueil.mp3")  
    pygame.mixer.music.play(-1)
    

    while True:
        ecran.blit(imageAccueil, (0,0))

        titre = policeTitre.render("Îles aux Fractions", True, noir)
        ecran.blit(titre, (largeurEcran // 2 - titre.get_width() // 2, hauteurEcran // 8))


        # Boutons
        largeurBouton, hauteurBouton = largeurEcran // 4, hauteurEcran // 10

        boutonJouer = bouton_texte("Jouer", 
                                   largeurEcran // 2 - largeurBouton // 2, 
                                   hauteurEcran // 3, 
                                   largeurBouton, 
                                   hauteurBouton, 
                                   bleue, blanc)
        boutonReglages = bouton_texte("Réglages", 
                                       largeurEcran // 2 - largeurBouton // 2, 
                                       hauteurEcran // 2, 
                                       largeurBouton, 
                                       hauteurBouton, 
                                       gris, blanc)
        boutonQuitter = bouton_texte("Quitter", 
                                  largeurEcran // 2 - largeurBouton // 2, 
                                  hauteurEcran * 2 // 3, 
                                  largeurBouton, 
                                  hauteurBouton, 
                                  rouge, blanc)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boutonJouer.collidepoint(event.pos):
                    pygame.mixer.music.stop()
                    pygame.time.wait(100) 
                    page_niveaux()  # Mène à la sélection des niveaux
                if boutonReglages.collidepoint(event.pos):
                    pygame.mixer.music.stop()
                    reglages()
                if boutonQuitter.collidepoint(event.pos):
                    pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()





# Page des réglages
def reglages():

    while True:
        ecran.fill(blanc)

        titre = policeTitre.render("Réglages", True, noir)
        ecran.blit(titre, (largeurEcran // 2 - titre.get_width() // 2, hauteurEcran // 8))

        button_width, button_height = largeurEcran // 4, hauteurEcran // 10
        boutonRetour = bouton_texte("Retour au menu", 
                                  largeurEcran // 2 - button_width // 2, 
                                  hauteurEcran * 2 // 3, 
                                  button_width, 
                                  button_height, 
                                  gris, blanc)
        
        boutonCreerTableur = bouton_texte("test_fichier", 
                                  largeurEcran // 2 - button_width // 2, 
                                  hauteurEcran  // 2, 
                                  button_width, 
                                  button_height, 
                                  gris, blanc)
        
        boutonRemplirTableur = bouton_texte("test_fichierremplir", 
                                  largeurEcran // 2 - button_width // 2, 
                                  hauteurEcran  // 3, 
                                  button_width, 
                                  button_height, 
                                  gris, blanc)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boutonRetour.collidepoint(event.pos):
                    pygame.mixer.music.load("son/musique_accueil.mp3")  
                    pygame.mixer.music.play(-1)
                    return
                if boutonCreerTableur.collidepoint(event.pos):
                    Creer_Tableur("test01")
                if boutonRemplirTableur.collidepoint(event.pos):
                    Remplir_Tableur("test01",1,"00001",1000,35,10)
                    print("ok")


                    

        pygame.display.flip()

# Menu de sélection des niveaux (va beaucoup changer donc pas à regarder)
def page_niveaux():
    global pieces

    while True:
        ecran.fill(blanc)

        titre = policeTitre.render("Sélection des niveaux", True, noir)
        ecran.blit(titre, (largeurEcran // 2 - titre.get_width() // 2, hauteurEcran // 10))

        # Afficher l'argent
        money_label = policeBase.render(f" {pieces} pièces d'or", True, jaune)
        ecran.blit(money_label, (largeurEcran - money_label.get_width() - 20, 20))

        # Dessiner les niveaux
        largeurBouton, hauteurBouton = largeurEcran // 3, hauteurEcran // 8
        for i in range(len(niveaux)):
            x = largeurEcran // 2 - (largeurBouton //2)
            y = hauteurEcran // 5 + (i % 5) * (hauteurBouton + hauteurEcran // 20)
            if niveaux[i]:  # Niveau débloqué
                color = vert
                level_text = f"Niveau {i + 1}"
            else:  # Niveau verrouillé
                color = gris
                level_text = f"Verrouillé ({10 * (i + 1)} pièces)"

            level_button = bouton_texte(level_text, x, y, largeurBouton, hauteurBouton, color, blanc)

            # Débloquer ou jouer
            if pygame.mouse.get_pressed()[0] and level_button.collidepoint(pygame.mouse.get_pos()):
                if niveaux[i]:
                    niveau_memory(i + 1)
                elif pieces >= 10 * (i + 1):  # Débloquer le niveau
                    pieces -= 10 * (i + 1)
                    niveaux[i] = True

        # Bouton Retour au menu
        back_button = bouton_texte("Retour au menu", 
                                  100, 
                                  hauteurEcran * 4 // 5, 
                                  largeurBouton//2, 
                                  hauteurBouton, 
                                  bleue, blanc)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    pygame.mixer.music.load("son/musique_accueil.mp3")  
                    pygame.mixer.music.play(-1)
                    return

        pygame.display.flip()




def niveau_memory(level):

    while True:
        ecran.fill(blanc)

        titre = policeTitre.render(f"Memory - Niveau {level}", True, noir)
        ecran.blit(titre, (largeurEcran // 2 - titre.get_width() // 2, hauteurEcran // 10))

        button_width, button_height = largeurEcran // 4, hauteurEcran // 10
        back_button = bouton_texte("Retour au menu", 
                                  largeurEcran // 2 - button_width // 2, 
                                  hauteurEcran * 4 // 5, 
                                  button_width, 
                                  button_height, 
                                  gris, blanc)
        
        play_button = bouton_texte("Jouer", 
                                   largeurEcran // 2 - button_width // 2, 
                                   hauteurEcran // 3, 
                                   button_width, 
                                   button_height, 
                                   bleue, blanc, 200)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    Memory()
                if back_button.collidepoint(event.pos):
                    return

        pygame.display.flip()

# Lancer le jeu
if __name__ == "__main__":
    menu()
