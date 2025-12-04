import pygame
from config import PLAYER_COLOR, PROJECTILE_COLOR, ENEMY_COLOR

class Player:
    def __init__(self, x, y, size, speed, screen_width):
        """
        Initialise le joueur avec une position, une taille et une vitesse.
        """
        self.rect = pygame.Rect(x, y, size, size)
        self.speed = speed
        self.screen_width = screen_width
        self.color = PLAYER_COLOR
        
    def move(self):
        """
        Déplace le joueur en fonction des touches pressées.
        """
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_q]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
            
        # S'assure que le joueur reste dans les limites de l'écran
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        
    def draw(self, screen):
        """
        Dessine le joueur sur l'écran.
        """
        pygame.draw.rect(screen, self.color, self.rect)

class Projectile:
    def __init__(self, x, y, size, speed, color=PROJECTILE_COLOR):
        """
        Initialise le projectile.
        """
        self.rect = pygame.Rect(x, y, size, size)
        self.speed = speed
        self.color = color

    def move(self):
        """
        Déplace le projectile vers le haut de l'écran.
        """
        self.rect.y -= self.speed

    def draw(self, screen):
        """
        Dessine le projectile sur l'écran.
        """
        pygame.draw.rect(screen, self.color, self.rect)

class Enemy:
    def __init__(self, x, y, size, speed, color=ENEMY_COLOR):
        """
        Classe de base pour tous les ennemis.
        """
        self.rect = pygame.Rect(x, y, size, size)
        self.speed = speed
        self.color = color
        self.direction = 1 # 1 pour droite, -1 pour gauche

    def move(self):
        """
        Logique de déplacement de base.
        Peut être surchargée par les classes filles.
        """
        self.rect.x += self.speed * self.direction

    def move_down(self, distance):
        """
        Fait descendre l'ennemi.
        """
        self.rect.y += distance

    def check_edges(self, screen_width):
        """
        Vérifie si l'ennemi touche un bord de l'écran.
        Retourne True si c'est le cas.
        """
        if self.rect.right >= screen_width:
            return True
        elif self.rect.left <= 0:
            return True
        return False

    def draw(self, screen):
        """
        Dessine l'ennemi.
        """
        pygame.draw.rect(screen, self.color, self.rect)

