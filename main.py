import pygame

# 1. Initialisation de Pygame
pygame.init()

# 2. Définir les dimensions de la fenêtre
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mon premier jeu Pygame")

# Création de l'horloge
clock = pygame.time.Clock()
# Limite de raffraichissement du jeu
refresh_rate = 60

# Définir un carré
player_size = 30
# On le positionne au centre de l'écran
# x = (largeur_ecran / 2) - (largeur_joueur / 2)
# y = (hauteur_ecran / 2) - (hauteur_joueur / 2)
player_pos = pygame.Rect(screen_width / 2 - player_size / 2, screen_height - 1.5 * player_size, player_size, player_size)
# Vitesse du joueur
player_speed = 5

#3 . La boucle de jeu principale (Game Loop)
running = True

while running:
    
    
    # 4. Gestion des événements
    for event in pygame.event.get():
        # Si l'utilisateur clique sur la croix pour fermer la fenêtre:
        if event.type == pygame.QUIT:
            running = False

    # 5. Logique du jeu
    
    # Récupère à chaque boucle l'état des touches. 
    keys = pygame.key.get_pressed()
    
    # Déplacement sur l'axe x
    if keys[pygame.K_LEFT]:
        player_pos.x -= player_speed 
    if keys[pygame.K_RIGHT]:
        player_pos.x += player_speed
    
    # Limiter le joueur aux bords de l'écran
    if player_pos.left < 0:
        player_pos.left = 0
    if player_pos.right > screen_width:
        player_pos.right = screen_width
        
    # 6. Dessiner sur l'écran
    # On remplit le fond en noir. Les couleurs sont en RGB
    screen.fill((0,0,0))

    # On dessine le carré (joueur) en blanc
    pygame.draw.rect(screen, (255, 255, 255), player_pos)
    
    # 7. Mettre à jour l'affichage
    pygame.display.flip()
    
    # Contrôler la vitesse de la boucle (FPS)
    clock.tick(refresh_rate)
    
# 8. Quitter Pygame
pygame.quit()