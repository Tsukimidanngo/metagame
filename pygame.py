#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# pacman_game.py
import pygame

# Initialize Pygame
pygame.init()

# Set up game constants
WIDTH, HEIGHT = 600, 600
FPS = 60

# Define colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")

# Set up Pac-Man
pacman_size = 30
pacman_x, pacman_y = WIDTH // 2, HEIGHT // 2
pacman_speed = 5

# Set up game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    pacman_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * pacman_speed
    pacman_y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * pacman_speed

    # Drawing
    screen.fill(WHITE)
    pygame.draw.circle(screen, YELLOW, (pacman_x, pacman_y), pacman_size)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()

