import pygame
import random

pygame.init()
clock = pygame.time.Clock()
running = True
screen_size = pygame.display.Info()
screen = pygame.display.set_mode((screen_size.current_w, screen_size.current_h), pygame.FULLSCREEN)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
