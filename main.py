import pygame
import sys
from data.fonctions_excel import *
from data.fonctions_mails import *
import random


pygame.init()


# Infos ecran
infoEcran = pygame.display.Info()
largeurEcran = infoEcran.current_w
hauteurEcran = infoEcran.current_h


# Configuration de l'affichage
ecran = pygame.display.set_mode((largeurEcran, hauteurEcran), pygame.SCALED | pygame.RESIZABLE)
pygame.display.set_caption("Îles aux fractions Edition MEMORY")





#Création des jeux de memorys par niveaux et en associant un nombre de paires en fonction du niveau.
matriceNiveaux = [
    #Niveau 1
    [
        [("1.png","chocolat1.png"),("1sur2.png","chocolat1sur2.png"),("1sur3.png","chocolat1sur3.png"),("1sur4.png","chocolat1sur4.png"),("2sur3.png","chocolat2sur3.png"),("3sur4.png","chocolat3sur4.png")]
        ],
    #Niveau 2
    [
        [("1sur1.png","chocolat1.png"),("1sur6.png","chocolat1sur6.png"),("1sur4.png","chocolat1sur4.png"),("3sur4.png","chocolat3sur4.png"),("5sur6.png","gateau5sur6.png"),("2sur3.png","gateau2sur3.png"),("1sur2.png","gateau1sur2.png"),("2sur6.png","gateau1sur3.png")],
     [("5sur6.png","chocolat5sur6.png"),("3sur6.png","chocolat1sur2.png"),("1sur4.png","chocolat1sur4.png"),("3sur4.png","chocolat3sur4.png"),("1.png","Gateau_entier.png"),("1sur3.png","gateau1sur3.png"),("4sur6.png","gateau2sur3.png"),("1sur6.png","gateau1sur6.png")],
     [("1sur3.png","chocolat1sur3.png"),("4sur6.png","chocolat2sur3.png"),("1sur4.png","chocolat1sur4.png"),("3sur4.png","chocolat3sur4.png"),("6sur6.png","Gateau_entier.png"),("5sur6.png","gateau5sur6.png"),("2sur4.png","gateau1sur2.png"),("1sur6.png","gateau1sur6.png")]
     ],
    #Niveau 3
    [
        [("1sur3.png","chocolat1sur3.png"),("7sur12.png","chocolat7sur12.png"),("3sur4.png","chocolat3sur4.png"),("1sur6.png","gateau1sur6.png"),("5sur6.png","gateau5sur6.png"),("3sur3.png","Gateau_entier.png"),("1sur12.png","oeuf1sur12.png"),("3sur6.png","oeuf6sur12.png"),("8sur12.png","oeuf8sur12.png"),("1sur4.png","oeuf3sur12.png")],
        [("5sur12.png","chocolat5sur12.png"),("3sur4.png","chocolat3sur4.png"),("1sur4.png","chocolat1sur4.png"),("1sur6.png","chocolat1sur6.png"),("5sur6.png","gateau5sur6.png"),("1sur2.png","gateau1sur2.png"),("2sur3.png","gateau2sur3.png"),("7sur12.png","oeuf7sur12.png"),("1sur12.png","oeuf1sur12.png"),("1.png","oeuf1sur1.png")],
        [("12sur12.png","chocolat1.png"),("9sur12.png","chocolat3sur4.png"),("2sur6.png","chocolat1sur3.png"),("2sur12.png","gateau1sur6.png"),("4sur6.png","gateau2sur3.png"),("1sur2.png","gateau1sur2.png"),("10sur12.png","oeuf10sur12.png"),("11sur12.png","oeuf11sur12.png"),("5sur12.png","oeuf5sur12.png"),("1sur4.png","oeuf3sur12.png")]
        ],
    #Niveau 4
    [
        [("1sur3.png","chocolat1sur3.png"),("5sur12.png","chocolat5sur12.png"),("3sur4.png","chocolat3sur4.png"),("1sur12.png","chocolat1sur12.png"),("1sur2.png","gateau1sur2.png"),("2sur3.png","gateau2sur3.png"),("1sur6.png","gateau1sur6.png"),("5sur6.png","gateau5sur6.png"),("1sur4.png","oeuf3sur12.png"),("11sur12.png","oeuf11sur12.png"),("7sur12.png","oeuf7sur12.png"),("1.png","oeuf1sur1.png")],
        [("1sur12.png","chocolat1sur12.png"),("1sur6.png","chocolat1sur6.png"),("4sur6.png","chocolat2sur3.png"),("3sur4.png","chocolat3sur4.png"),("2sur4.png","gateau1sur2.png"),("2sur6.png","gateau1sur3.png"),("1sur1.png","Gateau_entier.png"),("7sur12.png","oeuf7sur12.png"),("1sur4.png","oeuf3sur12.png"),("11sur12.png","oeuf11sur12.png"),("5sur6.png","oeuf10sur12.png"),("5sur12.png","oeuf5sur12.png")],
        [("5sur12.png","chocolat5sur12.png"),("11sur12.png","chocolat11sur12.png"),("6sur6.png","chocolat1.png"),("7sur12.png","chocolat7sur12.png"),("5sur6.png","gateau5sur6.png"),("1sur3.png","gateau1sur3.png"),("1sur6.png","gateau1sur6.png"),("1sur4.png","oeuf3sur12.png"),("1sur2.png","oeuf6sur12.png"),("3sur4.png","oeuf9sur12.png"),("2sur3.png","oeuf8sur12.png"),("1sur12.png","oeuf1sur12.png")]
        ],
    #Niveau 5
    [
        [("chocolat1sur6.png","gateau1sur6.png"),("chocolat1sur2.png","gateau1sur2.png"),("chocolat5sur6.png","gateau5sur6.png"),("gateau1sur3.png","oeuf4sur12.png"),("oeuf8sur12.png","gateau2sur3.png"),("oeuf1sur1.png","Gateau_entier.png"),("oeuf1sur12.png","chocolat1sur12.png"),("oeuf7sur12.png","chocolat7sur12.png"),("chocolat5sur12.png","oeuf5sur12.png"),("chocolat11sur12.png","oeuf11sur12.png"),("chocolat1sur4.png","oeuf3sur12.png"),("chocolat3sur4.png","oeuf9sur12.png")]
        ]
]


#Images
imageAccueil = pygame.image.load(chemin_exe("images/fond_ecran.jpg"))  
imageAccueil = pygame.transform.scale(imageAccueil, (largeurEcran, hauteurEcran))

imagefond1 = pygame.image.load(chemin_exe("images/fond1.png"))  
imagefond1 = pygame.transform.scale(imagefond1, (largeurEcran, hauteurEcran))

imagefond2 = pygame.image.load(chemin_exe("images/fond2.png"))  
imagefond2 = pygame.transform.scale(imagefond2, (largeurEcran, hauteurEcran))

imagefond3 = pygame.image.load(chemin_exe("images/fond3.png"))  
imagefond3 = pygame.transform.scale(imagefond3, (largeurEcran, hauteurEcran))

imagefond4 = pygame.image.load(chemin_exe("images/fond4.png"))  
imagefond4 = pygame.transform.scale(imagefond4, (largeurEcran, hauteurEcran))

imagefond5 = pygame.image.load(chemin_exe("images/fond5.png"))  
imagefond5 = pygame.transform.scale(imagefond5, (largeurEcran, hauteurEcran))

imagefond6 = pygame.image.load(chemin_exe("images/fond6.png"))  
imagefond6 = pygame.transform.scale(imagefond6, (largeurEcran, hauteurEcran))

imageboutonRouge = pygame.image.load(chemin_exe("images/boutonRouge.png"))  
imageboutonRouge= pygame.transform.scale(imageboutonRouge, (largeurEcran/(12.4*2), hauteurEcran/(7*2)))

imageboutonVert = pygame.image.load(chemin_exe("images/boutonVert.png"))  
imageboutonVert= pygame.transform.scale(imageboutonVert, (largeurEcran/(12.4*2), hauteurEcran/(7*2)))

imageboutonJaune = pygame.image.load(chemin_exe("images/boutonJaune.png")) 
imageboutonJaune= pygame.transform.scale(imageboutonJaune, (largeurEcran/(12.4*2), hauteurEcran/(7*2)))

imageCorde = pygame.image.load(chemin_exe("images/cadre_corde.png")) 
imageCorde= pygame.transform.scale(imageCorde, (largeurEcran/4.3, hauteurEcran/3))

imagePanneau = pygame.image.load(chemin_exe("images/indication_panneau.png")) 
imagePanneau= pygame.transform.scale(imagePanneau, (largeurEcran/1.7, hauteurEcran/2))

imagePanneauBloque = pygame.image.load(chemin_exe("images/panneau_bloque.png")) 
imagePanneauBloque= pygame.transform.scale(imagePanneauBloque, (largeurEcran/1.7, hauteurEcran/2))

bravo1 = pygame.image.load(chemin_exe("images/bravo1.png"))  
bravo1 = pygame.transform.scale(bravo1, (largeurEcran/1.7, hauteurEcran/2))

bravo2 = pygame.image.load(chemin_exe("images/bravo2.png"))  
bravo2 = pygame.transform.scale(bravo2, (largeurEcran/1.7, hauteurEcran/2))

bravo3 = pygame.image.load(chemin_exe("images/bravo3.png"))  
bravo3 = pygame.transform.scale(bravo3, (largeurEcran/1.7, hauteurEcran/2))

bravo4 = pygame.image.load(chemin_exe("images/bravo4.png"))  
bravo4 = pygame.transform.scale(bravo4, (largeurEcran/1.7, hauteurEcran/2))

bravo5 = pygame.image.load(chemin_exe("images/bravo5.png"))  
bravo5 = pygame.transform.scale(bravo5, (largeurEcran/1.7, hauteurEcran/2))

bravo6 = pygame.image.load(chemin_exe("images/bravo6.png"))  
bravo6 = pygame.transform.scale(bravo6, (largeurEcran/1.7, hauteurEcran/2))

imagefond=[imagefond1,imagefond2,imagefond3,imagefond4,imagefond5,imagefond6]
imageBravo=[bravo1,bravo2,bravo3,bravo4,bravo5,bravo6]

imageFondMemory = pygame.image.load(chemin_exe("images/fond_memory.jpg"))  
imageFondMemory = pygame.transform.scale(imageFondMemory, (largeurEcran, hauteurEcran))

dosCarte = pygame.image.load(chemin_exe("images/dos.png"))  
dosCarte = pygame.transform.scale(dosCarte, ((largeurEcran*(2/3)-60) // 6,(largeurEcran*(2/3)-60) // 6))




# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
gris = (100, 100, 100)
bleu = (0, 122, 204)
vert = (0, 204, 0)
rouge = (204, 0, 0)
jaune = (184,134,11)

# Police (possibilité d'en rajouter et de changer leur taille à partir de hauteurEcran)
policeTitre = pygame.font.SysFont('avenir', hauteurEcran // 10)
policeBase = pygame.font.SysFont('avenir', hauteurEcran // 20)




# Variables globales
niveaux = [False, False, False, False, False]   # suvi du déblocage des niveaux



# Fonction pour dessiner un bouton
def bouton_texte(texte, x, y, largeur, hauteur, couleur, couleurTexte, radius=200):
    pygame.draw.rect(ecran, couleur, (x, y, largeur, hauteur), border_radius=radius)
    label = policeBase.render(texte, True, couleurTexte)
    label_rect = label.get_rect(center=(x + largeur // 2, y + hauteur // 2))
    ecran.blit(label, label_rect)
    return pygame.Rect(x, y, largeur, hauteur)


# Fonction pour dessiner un bouton avec une image
def bouton_image ( image , x , y , largeur , hauteur ):
    image = pygame.image.load(chemin_exe(image))
    image = pygame.transform.scale(image,(largeur,hauteur))
    zoneCliquable = image.get_rect(topleft=(x,y))
    ecran.blit(image,zoneCliquable.topleft)
    return zoneCliquable


#Fonction qui affiche une animation quand on réussit un niveau (fonction trouvé sur Internet peut-être améliorée)
def animation_victoire(ecran): 
    pygame.mixer.music.load(chemin_exe("son/clap.wav"))
    pygame.mixer.music.play(1) 
    # Dégradé de couleurs (du blanc au doré)
    couleurs = [(255, 255, 255), (255, 215, 0)]
    texte = "Victoire !"
    
    # Préparation du texte
    font = pygame.font.SysFont('arial', 80, bold=True)
    texte_surface = font.render(texte, True, (255, 215, 0))
    texte_rect = texte_surface.get_rect(center=(largeurEcran // 2, hauteurEcran // 2))

    for alpha in range(0, 256, 3):
        # Calculer une couleur intermédiaire pour le fondu
        r = int((1 - alpha / 255) * couleurs[0][0] + (alpha / 255) * couleurs[1][0])
        g = int((1 - alpha / 255) * couleurs[0][1] + (alpha / 255) * couleurs[1][1])
        b = int((1 - alpha / 255) * couleurs[0][2] + (alpha / 255) * couleurs[1][2])
        
        surface = pygame.Surface((largeurEcran, hauteurEcran))
        surface.fill((r, g, b))
        surface.set_alpha(alpha)
        ecran.blit(surface, (0, 0))

        # Petit effet de zoom progressif sur le texte
        scale = 1 + alpha / 255 * 0.5  # Grossit jusqu’à 1.5x
        zoomed_surface = pygame.transform.scale(
            texte_surface,
            (int(texte_rect.width * scale), int(texte_rect.height * scale))
        )
        zoomed_rect = zoomed_surface.get_rect(center=(largeurEcran // 2, hauteurEcran // 2))
        ecran.blit(zoomed_surface, zoomed_rect)

        pygame.display.flip()
        pygame.time.delay(15)





# Page d'accueil
def menu():
    #Musique d'accueil
    pygame.mixer.init() 
    pygame.mixer.music.load(chemin_exe("son/musique_accueil.mp3"))  
    pygame.mixer.music.play(-1)

    Creer_Tableur() #Créer un nouveau tableur pour collecter les données des parties

    while True:
        ecran.blit(imageAccueil, (0,0))

        #Titre
        titre = policeTitre.render("Îles aux Fractions", True, noir)
        ecran.blit(titre, (largeurEcran // 2 - titre.get_width() // 2, hauteurEcran // 8))


        # Boutons
        largeurBouton, hauteurBouton = largeurEcran // 4, hauteurEcran // 10

        boutonJouer = bouton_texte("Jouer", 
                                   largeurEcran // 2 - largeurBouton // 2, 
                                   hauteurEcran // 3, 
                                   largeurBouton, 
                                   hauteurBouton, 
                                   bleu, blanc)
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
            if event.type == pygame.QUIT:  #Ferme la fenêtre avec la croix rouge
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  #gère les actions des boutons
                if boutonJouer.collidepoint(event.pos):
                    pygame.mixer.music.stop()
                    page_niveaux()  # Mène à la sélection des niveaux
                if boutonReglages.collidepoint(event.pos):
                    pygame.mixer.music.stop()
                    reglages() # Mène aux réglages
                if boutonQuitter.collidepoint(event.pos):
                    pygame.mixer.music.stop()
                    pygame.quit()  # Ferme l'application
                    sys.exit()

        pygame.display.flip()  #Actualise (important de la garder dans la boucle pour mettre à jour en continue l'écran et ses changements)



# Page des réglages
def reglages():
    envoie="non"
    while True:
        ecran.fill(blanc)

        titre = policeTitre.render("Réglages", True, noir)
        ecran.blit(titre, (largeurEcran // 2 - titre.get_width() // 2, hauteurEcran // 8))

        largeurBouton, hauteurBouton = largeurEcran // 4, hauteurEcran // 10

        boutonRetour = bouton_texte("Retour au menu", 
                                  largeurEcran // 2 - largeurBouton // 2, 
                                  hauteurEcran * 2 // 3, 
                                  largeurBouton, 
                                  hauteurBouton, 
                                  gris, blanc)
        
        if envoie=="non": #gère l'envoie pour envoyer les données une seule fois
            boutonEnvoyerData = bouton_texte("Récuperer les données", 
                                    largeurEcran // 2 - largeurBouton // 2, 
                                    hauteurEcran  // 3, 
                                    largeurBouton, 
                                    hauteurBouton, 
                                    bleu, blanc)
        elif envoie =="en cours":
            pygame.display.flip()  #enlever le bouton en actualisant
            envoie=EnvoyerMail()

        elif envoie == "envoyé":
            texte = policeTitre.render("Data envoyée !", True, vert)
            ecran.blit(texte, (largeurEcran // 2 - texte.get_width() // 2, hauteurEcran // 2))
        else:
            texte = policeTitre.render(envoie, True, rouge)
            ecran.blit(texte, (largeurEcran // 2 - texte.get_width() // 2, hauteurEcran // 2))
        


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boutonRetour.collidepoint(event.pos):
                    pygame.mixer.music.load(chemin_exe("son/musique_accueil.mp3"))  
                    pygame.mixer.music.play(-1)
                    return
                if boutonEnvoyerData.collidepoint(event.pos):
                    envoie="en cours"
                    



                    

        pygame.display.flip()



#Page de l'ile avec les différents niveaux
def page_niveaux():
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

    while True:
        #afficher le fond d'écran
        niveauEnCours = False
        if niveaux[4]:
            ecran.blit(imagefond[5], (0,0))
        else:
            for i in range(len(niveaux)):
                if not niveauEnCours:
                    if not niveaux[i]:
                        niveauEnCours = True
                        ecran.blit(imagefond[i], (0,0))
        
        #afficher les boutons rouges, jaunes ou verts
        niveauEnCoursBouton = False
        for i in range(len(niveaux)):
            if niveaux[i]:  
                boutons_niveaux[i] = bouton_image("images/boutonVert.png", x_bouton[i], y_bouton[i], largeurEcran / (12.4 * 2), hauteurEcran / (7 * 2))
                if pygame.mouse.get_pressed()[0] and boutons_niveaux[i].collidepoint(pygame.mouse.get_pos()):
                    niveau_memory(i)
            else:
                if not niveauEnCoursBouton:
                    boutons_niveaux[i] = bouton_image("images/boutonJaune.png", x_bouton[i], y_bouton[i], largeurEcran / (12.4 * 2), hauteurEcran / (7 * 2))
                    if pygame.mouse.get_pressed()[0] and boutons_niveaux[i].collidepoint(pygame.mouse.get_pos()):
                        niveau_memory(i)
                    niveauEnCoursBouton  = True
                else:
                    boutons_niveaux[i] = bouton_image("images/boutonRouge.png", x_bouton[i], y_bouton[i], largeurEcran / (12.4 * 2), hauteurEcran / (7 * 2))
                    if pygame.mouse.get_pressed()[0] and boutons_niveaux[i].collidepoint(pygame.mouse.get_pos()):
                        afficher_panneau_bloque = True


        # Bouton indication
        bouton_indication=bouton_image("images/indications.png", 0, 0, largeurEcran / (6 * 2), hauteurEcran / (4 * 2))
        if afficher_panneau:
            ecran.blit(imagePanneau, (largeurEcran / 4.8, hauteurEcran / 4))
            bouton_croix1 = bouton_image("images/croix.png", largeurEcran / 4.8 + imagePanneauBloque.get_width()*0.92, hauteurEcran / 4 - 40,largeurEcran / (6 * 2), hauteurEcran / (3.7 * 2))
        # Affichage du panneau bloqué + bouton croix
        if afficher_panneau_bloque:
            ecran.blit(imagePanneauBloque, (largeurEcran / 4.8, hauteurEcran / 4))
            bouton_croix2 = bouton_image("images/croix.png", largeurEcran / 4.8 + imagePanneauBloque.get_width()*0.92, hauteurEcran / 4 - 40,largeurEcran / (6 * 2), hauteurEcran / (3.7 * 2))
        
        # Bouton Retour au menu
        largeurBouton, hauteurBouton = largeurEcran // 6, hauteurEcran // 16
        boutonRetour = bouton_texte("Menu", 
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
                if boutonRetour.collidepoint(event.pos):
                    pygame.mixer.music.load(chemin_exe("son/musique_accueil.mp3"))  
                    pygame.mixer.music.play(-1)
                    return
                if afficher_panneau and bouton_croix1.collidepoint(event.pos):
                    afficher_panneau = False
                if bouton_indication.collidepoint(event.pos) and afficher_panneau==False:
                    afficher_panneau = True
                if afficher_panneau_bloque and bouton_croix2.collidepoint(event.pos):
                    afficher_panneau_bloque = False
        pygame.display.flip()



def niveau_memory(niveau):
     
    #Taille des cartes en carré
    coteCarte = (largeurEcran*(2/3)-60) // 6

    #Sélectionne un jeu parmis ceux disponibles
    tirageJeuCarte = random.randint(0, len(matriceNiveaux[niveau])-1)
    jeu_cartes = matriceNiveaux[niveau][tirageJeuCarte]

    paires_trouvees = 0
    nombreTentative = 0

    debutChrono = pygame.time.get_ticks()


    # Création de la liste des paires (on les duplique et mélange)
    paires = [(i, j) for i in range(len(jeu_cartes)) for j in (0, 1)]
    random.shuffle(paires)

    nbCartesLigne = 4 if len(paires) <= 16 else 5
    

    etat_cartes = ['cachee'] * len(paires)  # "cachee", "retournee", "trouvee"
    cartes_retournees = []  #stock les cartes faces visibles temporairement

    temps_retour = 0
    en_attente = False

    victoire=True
 

    while True:
        #Affichages
        ecran.blit(imageFondMemory, (0, 0))
        
        texte_paires = policeBase.render(f"Paires trouvées : {paires_trouvees}/{len(jeu_cartes)}", True, noir)
        ecran.blit(texte_paires, (largeurEcran*(210/300), hauteurEcran*(1/32)))

        texte_tentatives = policeBase.render(f"Tentatives : {nombreTentative}", True, noir)
        ecran.blit(texte_tentatives, (largeurEcran*(210/300), hauteurEcran*(6/32)))

        chrono = pygame.time.get_ticks() - debutChrono
        secondes = chrono // 1000
        minutes = secondes // 60
        secondesModulo = secondes % 60
        texte_temps = policeBase.render(f"{minutes:02}:{secondesModulo:02}", True, noir)
        ecran.blit(texte_temps, (largeurEcran*(210/300), hauteurEcran*(12/32)))  

        # Affichage des boutons
        largeurBouton, hauteurBouton = largeurEcran // 5.5, hauteurEcran // 10

        if victoire:
            boutonRetour = bouton_texte("Retour", (largeurEcran // 6)*5 - largeurBouton // 2,
                                    hauteurEcran * 4 // 5, largeurBouton, hauteurBouton, gris, blanc)


        listeZonesCliquables = []

        for index, (i, j) in enumerate(paires):
            #Placement des cartes
            x = (index % nbCartesLigne) * coteCarte + (index % nbCartesLigne + 1) * largeurEcran // 50
            y = (index // nbCartesLigne) * coteCarte + (index // nbCartesLigne + 1) * hauteurEcran // 80

            #Si la carte est retournee ou trouvee on l'affiche sinon une zone cliquable avec le dos de la carte
            if etat_cartes[index] in ['retournee', 'trouvee']:
                img_path = "images/" + jeu_cartes[i][j]
                img = pygame.image.load(chemin_exe(img_path))
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
                    Remplir_Tableur(secondes, nombreTentative, niveau+1, "non")
                    return

                for zone, idx in listeZonesCliquables:  #si on clique parmis les cartes cachés on la révèle
                    if zone.collidepoint(event.pos):
                        if etat_cartes[idx] == 'cachee' and len(cartes_retournees) < 2 and not en_attente:
                            etat_cartes[idx] = 'retournee'
                            cartes_retournees.append((idx, paires[idx]))


        # Si deux cartes retournées, on met en attente le temps de montrer les cartes
        if len(cartes_retournees) == 2 and not en_attente:
            temps_retour = pygame.time.get_ticks()
            en_attente = True

        # Une fois l'attente fini on compare les cartes
        if en_attente and pygame.time.get_ticks() - temps_retour > 600:
            idx1, (i1,j1) = cartes_retournees[0]
            idx2, (i2,j2) = cartes_retournees[1]

            nombreTentative+=1
            
            if i1 == i2:
                etat_cartes[idx1] = 'trouvee'
                etat_cartes[idx2] = 'trouvee'
                paires_trouvees += 1
            else:
                etat_cartes[idx1] = 'cachee'
                etat_cartes[idx2] = 'cachee'

            cartes_retournees.clear()
            en_attente = False

        #Instructions de victoire
        if paires_trouvees == len(jeu_cartes):
            if victoire:
                Remplir_Tableur(secondes, nombreTentative, niveau+1, "oui")
                pygame.mixer.music.play(1)  
                animation_victoire(ecran) 
                victoire=False
            ecran.blit(imageFondMemory, (0, 0))
            bouton_rejouer = bouton_texte("SUIVANT", largeurEcran*(1/2)- largeurBouton // 2, 5*hauteurEcran // 7,
                                        largeurBouton, hauteurBouton, vert, blanc)
            ecran.blit(imageBravo[niveau], (largeurEcran / 4.8, hauteurEcran / 6))
            if pygame.mouse.get_pressed()[0] and bouton_rejouer.collidepoint(pygame.mouse.get_pos()):
                    niveaux[niveau]=True
                    return

        pygame.display.flip()




# Lancer le jeu
if __name__ == "__main__":
    menu()
