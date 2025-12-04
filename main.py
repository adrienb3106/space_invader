import pygame
from classes import Player, Projectile
from config import *

def main():
    """
    Fonction principale du jeu.
    Initialise Pygame, crée la fenêtre, et gère la boucle de jeu.
    """
    # Initialisation de Pygame
    pygame.init()

    # --- Configuration de la fenêtre ---
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Jeu Pygame")

    # --- Horloge pour contrôler le taux de rafraîchissement ---
    clock = pygame.time.Clock()

    # --- Création du joueur ---
    # Position initiale : au centre en bas de l'écran
    start_x = (SCREEN_WIDTH / 2) - (PLAYER_SIZE / 2)
    start_y = SCREEN_HEIGHT - (1.5 * PLAYER_SIZE)
    player = Player(start_x, start_y, PLAYER_SIZE, PLAYER_SPEED, SCREEN_WIDTH)

    # --- Liste pour les projectiles ---
    projectiles = []

    # --- Boucle de jeu principale ---
    running = True
    while running:
        # --- Gestion des événements ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Gestion du tir
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    proj_x = player.rect.centerx - (PROJECTILE_SIZE / 2)
                    proj_y = player.rect.top
                    new_projectile = Projectile(proj_x, proj_y, PROJECTILE_SIZE, PROJECTILE_SPEED)
                    projectiles.append(new_projectile)

        # --- Mises à jour logiques ---
        player.move()
        
        # Mouvement des projectiles
        for proj in projectiles:
            proj.move()

        # Suppression des projectiles hors de l'écran
        projectiles = [proj for proj in projectiles if proj.rect.bottom > 0]

        # --- Rendu graphique ---
        screen.fill(BLACK)
        
        player.draw(screen)
        
        # Dessin des projectiles
        for proj in projectiles:
            proj.draw(screen)

        # Mettre à jour l'affichage
        pygame.display.flip()

        # Limiter le taux de rafraîchissement
        clock.tick(FPS)

    # --- Fin du jeu ---
    pygame.quit()


if __name__ == "__main__":
    main()