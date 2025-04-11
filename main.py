import pygame
import sys
from memory import Memory
from data.fonctions_excel import *

import time
import textwrap
pygame.init()


# Infos ecran
infoEcran = pygame.display.Info()
largeurEcran = infoEcran.current_w
hauteurEcran = infoEcran.current_h

matriceNiveaux = [
    [[("1.png","chocolat1.png"),("1sur2.png","chocolat1sur2.png"),("1sur3.png","chocolat1sur3.png"),("1sur4.png","chocolat1sur4.png"),("2sur3.png","chocolat2sur3.png"),("3sur4.png","chocolat3sur4.png")]],
    [[("1sur1.png","chocolat1.png"),("1sur6.png","chocolat1sur6.png"),("1sur4.png","chocolat1sur4.png"),("3sur4.png","chocolat3sur4.png"),("5sur6.png","gateau5sur6.png"),("2sur3.png","gateau2sur3.png"),("1sur2.png","gateau1sur2.png"),("2sur6.png","gateau1sur3.png")],[("5sur6.png","chocolat5sur6.png"),("3sur6.png","chocolat1sur2.png"),("1sur4.png","chocolat1sur4.png"),("3sur4.png","chocolat3sur4.png"),("1.png","Gateau_entier.png"),("1sur3.png","gateau1sur3.png"),("4sur6.png","gateau2sur3.png"),("1sur6.png","gateau1sur6.png")],[("1sur3.png","chocolat1sur3.png"),("4sur6.png","chocolat2sur3.png"),("1sur4.png","chocolat1sur4.png"),("3sur4.png","chocolat3sur4.png"),("6sur6.png","Gateau_entier.png"),("5sur6.png","gateau5sur6.png"),("2sur4.png","gateau1sur2.png"),("1sur6.png","gateau1sur6.png")]],
    [[("1sur3.png","chocolat1sur3.png"),("7sur12.png","chocolat7sur12.png"),("3sur4.png","chocolat3sur4.png"),("1sur6.png","gateau1sur6.png"),("5sur6.png","gateau5sur6.png"),("3sur3.png","Gateau_entier.png"),("1sur12.png","oeuf1sur12.png"),("3sur6.png","oeuf6sur12.png"),("8sur12.png","oeuf8sur12.png"),("1sur4.png","oeuf3sur12.png")],[("5sur12.png","chocolat5sur12.png"),("3sur4.png","chocolat3sur4.png"),("1sur4.png","chocolat1sur4.png"),("1sur6.png","chocolat1sur6.png"),("5sur6.png","gateau5sur6.png"),("1sur2.png","gateau1sur2.png"),("2sur3.png","gateau2sur3.png"),("7sur12.png","oeuf7sur12.png"),("1sur12.png","oeuf1sur12.png"),("1.png","oeuf1sur1.png")],[("12sur12.png","chocolat1.png"),("9sur12.png","chocolat3sur4.png"),("2sur6.png","chocolat1sur3.png"),("2sur12.png","gateau1sur6.png"),("4sur6.png","gateau2sur3.png"),("1sur2.png","gateau1sur2.png"),("10sur12.png","oeuf10sur12.png"),("11sur12.png","oeuf11sur12.png"),("5sur12.png","oeuf5sur12.png"),("1sur4.png","oeuf3sur12.png")]],
    [[("1sur3.png","chocolat1sur3.png"),("5sur12.png","chocolat5sur12.png"),("3sur4.png","chocolat3sur4.png"),("1sur12.png","chocolat1sur12.png"),("1sur2.png","gateau1sur2.png"),("2sur3.png","gateau2sur3.png"),("1sur6.png","gateau1sur6.png"),("5sur6.png","gateau5sur6.png"),("1sur4.png","oeuf3sur12.png"),("11sur12.png","oeuf11sur12.png"),("7sur12.png","oeuf7sur12.png"),("1.png","oeuf1sur1.png")],[("1sur12.png","chocolat1sur12.png"),("1sur6.png","chocolat1sur6.png"),("4sur6.png","chocolat2sur3.png"),("3sur4.png","chocolat3sur4.png"),("2sur4.png","gateau1sur2.png"),("2sur6.png","gateau1sur3.png"),("1sur1.png","Gateau_entier.png"),("7sur12.png","oeuf7sur12.png"),("1sur4.png","oeuf3sur12.png"),("11sur12.png","oeuf11sur12.png"),("5sur6.png","oeuf10sur12.png"),("5sur12.png","oeuf5sur12.png")],[("5sur12.png","chocolat5sur12.png"),("11sur12.png","chocolat11sur12.png"),("6sur6.png","chocolat1.png"),("7sur12.png","chocolat7sur12.png"),("5sur6.png","gateau5sur6.png"),("1sur3.png","gateau1sur3.png"),("1sur6.png","gateau1sur6.png"),("1sur4.png","oeuf3sur12.png"),("1sur2.png","oeuf6sur12.png"),("3sur4.png","oeuf9sur12.png"),("2sur3.png","oeuf8sur12.png"),("1sur12.png","oeuf1sur12.png")]],
    [[("chocolat1sur6.png","gateau1sur6.png"),("chocolat1sur2.png","gateau1sur2.png"),("chocolat5sur6.png","gateau5sur6.png"),("gateau1sur3.png","oeuf4sur12.png"),("oeuf8sur12.png","gateau2sur3.png"),("oeuf1sur1.png","Gateau_entier.png"),("oeuf1sur12.png","chocolat1sur12.png"),("oeuf5sur12.png","chocolat5sur12.png"),("chocolat5sur12.png","oeuf5sur12.png"),("chocolat11sur12.png","oeuf11sur12.png"),("chocolat1sur4.png","oeuf3sur12.png"),("chocolat3sur4.png","oeuf9sur12.png")]]
]

# Configuration de l'affichage
ecran = pygame.display.set_mode((largeurEcran, hauteurEcran), pygame.SCALED | pygame.RESIZABLE)
pygame.display.set_caption("Îles aux fractions Memory")


#Images
imageAccueil = pygame.image.load("images/fond_ecran.jpg")  
imageAccueil = pygame.transform.scale(imageAccueil, (largeurEcran, hauteurEcran))
imagefond1 = pygame.image.load("images/fond1.png")  
imagefond1 = pygame.transform.scale(imagefond1, (largeurEcran, hauteurEcran))
imagefond2 = pygame.image.load("images/fond2.png")  
imagefond2 = pygame.transform.scale(imagefond2, (largeurEcran, hauteurEcran))
imagefond3 = pygame.image.load("images/fond3.png")  
imagefond3 = pygame.transform.scale(imagefond3, (largeurEcran, hauteurEcran))
imagefond4 = pygame.image.load("images/fond4.png")  
imagefond4 = pygame.transform.scale(imagefond4, (largeurEcran, hauteurEcran))
imagefond5 = pygame.image.load("images/fond5.png")  
imagefond5 = pygame.transform.scale(imagefond5, (largeurEcran, hauteurEcran))
imagefond6 = pygame.image.load("images/fond6.png")  
imagefond6 = pygame.transform.scale(imagefond6, (largeurEcran, hauteurEcran))
imageboutonRouge = pygame.image.load("images/boutonRouge.png")  
imageboutonRouge= pygame.transform.scale(imageboutonRouge, (largeurEcran/(12.4*2), hauteurEcran/(7*2)))
imageboutonVert = pygame.image.load("images/boutonVert.png")  
imageboutonVert= pygame.transform.scale(imageboutonVert, (largeurEcran/(12.4*2), hauteurEcran/(7*2)))
imageboutonJaune = pygame.image.load("images/boutonJaune.png") 
imageboutonJaune= pygame.transform.scale(imageboutonJaune, (largeurEcran/(12.4*2), hauteurEcran/(7*2)))
imageCorde = pygame.image.load("images/cadre_corde.png") 
imageCorde= pygame.transform.scale(imageCorde, (largeurEcran/4.3, hauteurEcran/3))
imagePanneau = pygame.image.load("images/indication_panneau.png") 
imagePanneau= pygame.transform.scale(imagePanneau, (largeurEcran/1.7, hauteurEcran/2))
imagePanneauBloque = pygame.image.load("images/panneau_bloque.png") 
imagePanneauBloque= pygame.transform.scale(imagePanneauBloque, (largeurEcran/1.7, hauteurEcran/2))

imagefond=[imagefond1,imagefond2,imagefond3,imagefond4,imagefond5,imagefond6]



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
niveaux = [True, True, False, False, False]   

# Fonction pour dessiner un bouton
def bouton_texte(texte, x, y, largeur, hauteur, couleur, couleurTexte, radius=200):
    pygame.draw.rect(ecran, couleur, (x, y, largeur, hauteur), border_radius=radius)
    label = policeBase.render(texte, True, couleurTexte)
    label_rect = label.get_rect(center=(x + largeur // 2, y + hauteur // 2))
    ecran.blit(label, label_rect)
    return pygame.Rect(x, y, largeur, hauteur)


# Charger l'image du bouton
def bouton_image ( image , x , y , largeur , hauteur ):
    image = pygame.image.load (image)
    image = pygame.transform.scale(image,(largeur,hauteur))
    zoneCliquable = image.get_rect(topleft=(x,y))
    ecran.blit(image,zoneCliquable.topleft)
    return zoneCliquable

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
                    page_niveaux2()  # Mène à la sélection des niveaux
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

#def boutons principaux page de niveaux
x_bouton=[largeurEcran/3.2,largeurEcran/2.83,largeurEcran*2/3.87,largeurEcran*2/3.35,largeurEcran*2.68/3.8]
y_bouton=[hauteurEcran/5.8,hauteurEcran/2.15,hauteurEcran*2/3.6, hauteurEcran/4.75,hauteurEcran*2/3.2]

boutons_niveaux = [bouton_image("images/boutonRouge.png", x_bouton[0], y_bouton[0], largeurEcran / (12.4 * 2), hauteurEcran / (7 * 2)),
                    bouton_image("images/boutonRouge.png", x_bouton[1], y_bouton[1], largeurEcran / (12.4 * 2), hauteurEcran / (7 * 2)),
                    bouton_image("images/boutonRouge.png", x_bouton[2], y_bouton[2], largeurEcran / (12.4 * 2), hauteurEcran / (7 * 2)),
                    bouton_image("images/boutonRouge.png", x_bouton[3], y_bouton[3], largeurEcran / (12.4 * 2), hauteurEcran / (7 * 2)),
                    bouton_image("images/boutonRouge.png", x_bouton[4], y_bouton[4], largeurEcran / (12.4 * 2), hauteurEcran / (7 * 2))
                    ]

afficher_panneau = False
afficher_panneau_bloque = False

#Page de l'ile avec les différents niveaux
def page_niveaux2():
    while True:

        global afficher_panneau, afficher_panneau_bloque

        #afficher le fond d'écran
        premier_false_trouve1 = False
        if niveaux[4]:
            ecran.blit(imagefond[5], (0,0))
        else:
            for i in range(len(niveaux)):
                if not premier_false_trouve1:
                    if not niveaux[i]:
                        premier_false_trouve1 = True
                        ecran.blit(imagefond[i], (0,0))
        
        #afficher les boutons rouges, jaunes ou verts
        premier_false_trouve2 = False
        for i in range(len(niveaux)):
            if niveaux[i]:  
                boutons_niveaux[i] = bouton_image("images/boutonVert.png", x_bouton[i], y_bouton[i], largeurEcran / (12.4 * 2), hauteurEcran / (7 * 2))
                if pygame.mouse.get_pressed()[0] and boutons_niveaux[i].collidepoint(pygame.mouse.get_pos()):
                    niveau_memory(1)
            else:
                if not premier_false_trouve2:
                    boutons_niveaux[i] = bouton_image("images/boutonJaune.png", x_bouton[i], y_bouton[i], largeurEcran / (12.4 * 2), hauteurEcran / (7 * 2))
                    if pygame.mouse.get_pressed()[0] and boutons_niveaux[i].collidepoint(pygame.mouse.get_pos()):
                        niveau_memory(1)
                    premier_false_trouve2 = True
                else:
                    boutons_niveaux[i] = bouton_image("images/boutonRouge.png", x_bouton[i], y_bouton[i], largeurEcran / (12.4 * 2), hauteurEcran / (7 * 2))
                    if pygame.mouse.get_pressed()[0] and boutons_niveaux[i].collidepoint(pygame.mouse.get_pos()):
                        afficher_panneau_bloque = True


        # Bouton indication
        bouton_indication=bouton_image("images/indications.png", 0, 0, largeurEcran / (6 * 2), hauteurEcran / (4 * 2))
        if afficher_panneau:
            ecran.blit(imagePanneau, (largeurEcran / 4.8, hauteurEcran / 4))

        # Affichage du panneau bloqué + bouton croix
        if afficher_panneau_bloque:
            ecran.blit(imagePanneauBloque, (largeurEcran / 4.8, hauteurEcran / 4))
            bouton_croix = bouton_image("images/croix.png", largeurEcran / 4.8 + imagePanneauBloque.get_width()*0.92, hauteurEcran / 4 - 40,largeurEcran / (6 * 2), hauteurEcran / (3.7 * 2))
        
        # Bouton Retour au menu
        largeurBouton, hauteurBouton = largeurEcran // 6, hauteurEcran // 16
        back_button = bouton_texte("Menu", 
                                  largeurEcran/30, 
                                  hauteurEcran * 4.5 // 5, 
                                  largeurBouton//2, 
                                  hauteurBouton, 
                                  noir, blanc)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    pygame.mixer.music.load("son/musique_accueil.mp3")  
                    pygame.mixer.music.play(-1)
                    return
                if bouton_indication.collidepoint(event.pos):
                    afficher_panneau = not afficher_panneau
                if afficher_panneau_bloque and bouton_croix.collidepoint(event.pos):
                    afficher_panneau_bloque = False
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
