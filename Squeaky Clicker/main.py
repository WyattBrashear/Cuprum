import pygame
import random
import time

pygame.init()
clock = pygame.time.Clock()
running = True
screen = pygame.display.set_mode((1080, 1920), pygame.FULLSCREEN)
pygame.display.set_caption('Squeaky Clicker - Made For Cuprum')
center_h = 300
center_w = 0

logo_shown = False
screen.fill((0, 0, 0))
pygame.display.flip()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #YES I KNOW THIS IS INNEFICIENT. Ill fix it later
    if not logo_shown:
        for i in range(255):
            screen.fill((i, i, i))
            time.sleep(0.01)
            pygame.display.flip()
        for i in range(100):
            screen.fill((255, 255, 255))
            x = random.randint(1, 3)
            logo = pygame.image.load(f'./assets/branding/Logo{x}.png')
            screen.blit(logo, (center_h, center_w))
            pygame.display.flip()
            time.sleep(0.05)
        for i in range(255):
            screen.fill((255-i, 255-i, 255-i))
            time.sleep(0.01)
            pygame.display.flip()
        logo_shown = True
    pygame.display.flip()
