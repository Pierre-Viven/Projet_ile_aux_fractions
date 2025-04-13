import pygame
import sys
from memory import Memory
from data.fonctions_excel import *
import random
import time

pygame.init()

def animation_victoire(ecran):
    surface = pygame.Surface((largeurEcran, hauteurEcran))
    surface.fill((255, 255, 255))
    for alpha in range(0, 255, 5):
        surface.set_alpha(alpha)
        ecran.blit(surface, (0, 0))
        pygame.display.flip()
        pygame.time.delay(10)   


# Infos ecran
infoEcran = pygame.display.Info()
largeurEcran = infoEcran.current_w
hauteurEcran = infoEcran.current_h

# Configuration de l'affichage
ecran = pygame.display.set_mode((largeurEcran, hauteurEcran), pygame.SCALED | pygame.RESIZABLE)
pygame.display.set_caption("Îles aux fractions Memory")

matriceNiveaux = [
    [[("1sur1.png","chocolat1.png"),("1sur2.png","chocolat1sur2.png"),("1sur3.png","chocolat1sur3.png"),("1sur4.png","chocolat1sur4.png"),("2sur3.png","chocolat2sur3.png"),("3sur4.png","chocolat3sur4.png")]],
    [[],[]],
    [[],[]],
    [[],[]],
    [[],[]]
]


#Images
imageAccueil = pygame.image.load("images/fond_ecran.jpg")  
imageAccueil = pygame.transform.scale(imageAccueil, (largeurEcran, hauteurEcran))

imageFondMemory = pygame.image.load("images/fond_memory.jpg")  
imageFondMemory = pygame.transform.scale(imageFondMemory, (largeurEcran*(2/3), hauteurEcran))

dosCarte = pygame.image.load("images/dos.png")  
dosCarte = pygame.transform.scale(dosCarte, ((largeurEcran*(2/3)-60) // 6,(largeurEcran*(2/3)-60) // 6))


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




# Charger l'image du bouton
def bouton_image(image, x, y, largeur, hauteur):
    image = pygame.image.load(image)
    image = pygame.transform.scale(image, (largeur, hauteur))
    zoneCliquable = image.get_rect(topleft=(x, y))
    ecran.blit(image, zoneCliquable)
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
                    niveau_memory2(0)
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

        ecran.fill()

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



def niveau_memory2(niveau):
    jeu_carte = random.randint(0, len(matriceNiveaux[niveau]) - 1)
    cartes_data = matriceNiveaux[niveau][jeu_carte]
    nb_cartes = len(cartes_data)

    paires_trouvees = 0
    total_paires = len(cartes_data)

    # Création de la liste des paires (on les duplique et mélange)
    paires = [(i, j) for i in range(nb_cartes) for j in (0, 1)]
    random.shuffle(paires)

    nbCartesLigne = 4 if len(paires) <= 16 else 5
    coteCarte = (largeurEcran*(2/3)-60) // 6

    etat_cartes = ['cachee'] * len(paires)  # "cachee", "retournee", "trouvee"
    cartes_retournees = []  # [(index, (i, j))]

    clock = pygame.time.Clock()

    cartes_retournees = []
    temps_retour = 0
    en_attente = False

    etat_jeu = "en_cours"


    while True:
        ecran.fill(blanc)
        ecran.blit(imageFondMemory, (0, 0))
        texte_paires = policeBase.render(f"Paires trouvées : {paires_trouvees}/{total_paires}", True, noir)
        ecran.blit(texte_paires, (largeurEcran*(210/300), hauteurEcran*(1/32)))

        # Affichage des boutons
        largeurBouton, hauteurBouton = largeurEcran // 5.5, hauteurEcran // 10
        boutonRetour = bouton_texte("Retour aux niveaux", (largeurEcran // 6)*5 - largeurBouton // 2,
                                    hauteurEcran * 4 // 5, largeurBouton, hauteurBouton, gris, blanc)


        listeZonesCliquables = []

        for index, (i, j) in enumerate(paires):
            x = (index % nbCartesLigne) * coteCarte + (index % nbCartesLigne + 1) * largeurEcran // 50
            y = (index // nbCartesLigne) * coteCarte + (index // nbCartesLigne + 1) * hauteurEcran // 80

            etat = etat_cartes[index]

            if etat in ['retournee', 'trouvee']:
                img_path = "images/" + cartes_data[i][j]
                img = pygame.image.load(img_path)
                img = pygame.transform.scale(img, (int(coteCarte), int(coteCarte)))
                ecran.blit(img, (x, y))
            else:
                zone = bouton_image("images/dos.png", x, y, coteCarte, coteCarte)
                listeZonesCliquables.append((zone, index))

        # Gestion clics
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if boutonRetour.collidepoint(event.pos):
                    return

                for zone, idx in listeZonesCliquables:
                    if zone.collidepoint(event.pos):
                        if etat_cartes[idx] == 'cachee' and len(cartes_retournees) < 2 and not en_attente:
                            etat_cartes[idx] = 'retournee'
                            cartes_retournees.append((idx, paires[idx]))


        # Si deux cartes retournées, on vérifie
        # Si 2 cartes retournées mais on attend le délai
        if len(cartes_retournees) == 2 and not en_attente:
            temps_retour = pygame.time.get_ticks()
            en_attente = True

        # Si on a attendu suffisamment (ex: 800 ms), on peut comparer les cartes
        if en_attente and pygame.time.get_ticks() - temps_retour > 800:
            idx1, (i1, j1) = cartes_retournees[0]
            idx2, (i2, j2) = cartes_retournees[1]

            print("Carte 1 :", cartes_data[i1][j1], "| Carte 2 :", cartes_data[i2][j2])
            if i1 == i2:
                etat_cartes[idx1] = 'trouvee'
                etat_cartes[idx2] = 'trouvee'
                paires_trouvees += 1
            else:
                etat_cartes[idx1] = 'cachee'
                etat_cartes[idx2] = 'cachee'

            cartes_retournees.clear()
            en_attente = False


        if paires_trouvees == total_paires:
            etat_jeu = "gagne"
            texte_victoire = policeBase.render("Bravo !", True, vert)
            ecran.blit(texte_victoire, (largeurEcran*(5/6) - texte_victoire.get_width() // 2, hauteurEcran // 4))

            bouton_rejouer = bouton_texte("Rejouer", largeurEcran*(5/6)- largeurBouton // 2, hauteurEcran // 2,
                                        largeurBouton, hauteurBouton, vert, blanc)




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if etat_jeu == "gagne":
                    if bouton_rejouer.collidepoint(event.pos):
                        niveau_memory2(niveau)  # relancer la fonction depuis le début
                        return
                if bouton_rejouer.collidepoint(event.pos):
                    niveau_memory2(niveau)
                if boutonRetour.collidepoint(event.pos):
                    return

        pygame.display.flip()




# Lancer le jeu
if __name__ == "__main__":
    menu()
