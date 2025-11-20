import pygame

# 1. Initialisation de Pygame
pygame.init()

# 2. Définir les dimensions de la fenêtre
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mon premier jeu Pygame")

#3 . La boucle de jeu principale (Game Loop)
running = True

while running:
    # 4. Gestion des événements
    for event in pygame.event.get():
        # Si l'utilisateur clique sur la croix pour fermer la fenêtre:
        if event.type == pygame.QUIT:
            running = False
            
    # 5. Logique du jeu (pour l'instant, rien)
    
    # 6. Dessiner sur l'écran
    # On remplit le fond en noir. Les couleurs sont en RGB
    screen.fill((0,0,0))
    
    # 7. Mettre à jour l'affichage
    pygame.display.flip()
    
# 8. Quitter Pygame
pygame.quit()