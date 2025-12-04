import pygame
from classes import Player, Projectile, Enemy
from config import *

def create_fleet():
    """
    Crée une flotte d'ennemis et les retourne dans un dictionnaire.
    """
    enemies = {}
    enemy_id = 0
    for row in range(ENEMY_ROWS):
        for col in range(ENEMY_COLS):
            # Calcul de la position
            x = 50 + col * (ENEMY_SIZE + ENEMY_PADDING)
            y = 50 + row * (ENEMY_SIZE + ENEMY_PADDING)
            
            new_enemy = Enemy(x, y, ENEMY_SIZE, ENEMY_SPEED)
            enemies[enemy_id] = new_enemy
            enemy_id += 1
    return enemies

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

    # --- Création de la flotte d'ennemis ---
    enemies = create_fleet()

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
        
        # Logique de déplacement de la flotte
        fleet_touched_edge = False
        for enemy in enemies.values():
            if enemy.check_edges(SCREEN_WIDTH):
                fleet_touched_edge = True
                break
        
        if fleet_touched_edge:
            for enemy in enemies.values():
                enemy.direction *= -1
                enemy.move_down(DESCENT_SPEED)
        
        for enemy in enemies.values():
            enemy.move()
        
        # Mouvement des projectiles
        for proj in projectiles:
            proj.move()

        # Suppression des projectiles hors de l'écran
        projectiles = [proj for proj in projectiles if proj.rect.bottom > 0]

        # --- Gestion des collisions ---
        # Projectile <-> Ennemi
        projectiles_to_remove = []
        enemies_to_remove = []

        for proj in projectiles:
            for enemy_id, enemy in enemies.items():
                if proj.rect.colliderect(enemy.rect):
                    projectiles_to_remove.append(proj)
                    enemies_to_remove.append(enemy_id)
                    break # Un projectile ne touche qu'un seul ennemi

        # Suppression des éléments touchés
        for proj in projectiles_to_remove:
            if proj in projectiles:
                projectiles.remove(proj)
        
        for enemy_id in enemies_to_remove:
            if enemy_id in enemies:
                del enemies[enemy_id]

        # --- Rendu graphique ---
        screen.fill(BLACK)
        
        player.draw(screen)
        
        for enemy in enemies.values():
            enemy.draw(screen)
        
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