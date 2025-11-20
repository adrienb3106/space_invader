# Roadmap du Projet "Pygame Invaders"

Ce document décrit les étapes de développement prévues pour le jeu, en partant de la base existante.

## Phase 1 : Les bases du jeu (✅ Terminé)

- [x] Initialisation de la fenêtre Pygame.
- [x] Création du vaisseau du joueur (un carré).
- [x] Gestion du déplacement horizontal du joueur via le clavier.
- [x] Contrôle de la vitesse de rafraîchissement (FPS) pour un mouvement constant.
- [x] Limitation du joueur aux bords de l'écran.
- [x] Positionnement initial du joueur en bas de l'écran.

## Phase 2 : Mécaniques de tir et ennemis

- [ ] **Refactorisation en classes**
  - [ ] Transformer le joueur en une classe `Player` pour mieux organiser le code.
- [ ] **Tir du joueur**
  - [ ] Créer une classe `Projectile`.
  - [ ] Permettre au joueur de tirer (ex: avec la barre d'espace).
  - [ ] Gérer le déplacement vertical des projectiles.
  - [ ] Gérer la suppression des projectiles qui sortent de l'écran.
- [ ] **Création des ennemis**
  - [ ] Créer une classe `Enemy`.
  - [ ] Faire apparaître une ligne ou une grille d'ennemis en haut de l'écran.
  - [ ] Gérer le déplacement latéral du bloc d'ennemis.
  - [ ] Faire descendre les ennemis lorsqu'ils touchent un bord de l'écran.

## Phase 3 : Gameplay et interface

- [ ] **Gestion des collisions**
  - [ ] Détecter la collision entre un projectile du joueur et un ennemi.
  - [ ] Supprimer l'ennemi et le projectile lors d'une collision.
- [ ] **Système de score et de vies**
  - [ ] Augmenter le score quand un ennemi est détruit.
  - [ ] Afficher le score à l'écran.
  - [ ] Mettre en place un système de vies pour le joueur.
- [ ] **Conditions de victoire et de défaite**
  - [ ] Détecter quand un ennemi atteint le bas de l'écran (Game Over).
  - [ ] Détecter quand tous les ennemis d'une vague sont détruits (Niveau suivant).
  - [ ] Afficher un écran "Game Over" ou "Niveau Terminé".

## Phase 4 : Améliorations et finitions

- [ ] **Tir des ennemis**
  - [ ] Permettre aux ennemis de tirer aléatoirement des projectiles vers le bas.
  - [ ] Gérer la collision entre un projectile ennemi et le joueur.
- [ ] **Audio**
  - [ ] Ajouter des effets sonores (tir, explosion).
  - [ ] Ajouter une musique de fond.
- [ ] **Graphismes**
  - [ ] Remplacer les formes géométriques par des images (sprites).
