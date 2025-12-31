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
squeaker_level = 1
points = 0
dog_level = 0
logo_shown = False
screen.fill((0, 0, 0))
pygame.display.flip()
squeaker = pygame.image.load(f'./assets/squeakers/squeaky{squeaker_level}.png')
points_font = pygame.font.SysFont('Comic Sans MS', 50)
item_font = pygame.font.SysFont('Comic Sans MS', 30)
rotation_a = True
additional_number = random.randint(1, 10)
while running:
    dog_cost = dog_level+1
    dog_cost *= 35
    dog_cost += additional_number
    squeaker_cost = squeaker_level*20
    squeaker_cost += additional_number
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                points_tobeadded = 1*squeaker_level
                points += points_tobeadded
            if event.key == pygame.K_0:
                points_toberemoved = squeaker_level*20
                if int(points) >= points_toberemoved:
                    squeaker_level += 1
                    print(points_toberemoved)
                    points -= points_toberemoved+additional_number
                    additional_number = random.randint(1, 10)
                else:
                    print("Not Enough Squeaks to purchase this upgrade!")
            if event.key == pygame.K_1:
                points_toberemoved = dog_level+1
                points_toberemoved *= 35
                if int(points) >= points_toberemoved:
                    dog_level += 1
                    print(points_toberemoved)
                    points -= points_toberemoved+additional_number
                    additional_number = random.randint(1, 10)
                else:
                    print("Not Enough Squeaks to purchase this upgrade!")
    if not logo_shown:
        for i in range(255):
            screen.fill((i, i, i))
            time.sleep(0.007)
            pygame.display.flip()
        for i in range(75):
            screen.fill((255, 255, 255))
            x = random.randint(1, 3)
            logo = pygame.image.load(f'./assets/branding/Logo{x}.png')
            screen.blit(logo, (center_h, center_w))
            pygame.display.flip()
            time.sleep(0.02)
        for i in range(255):
            screen.fill((255-i, 255-i, 255-i))
            time.sleep(0.007)
            pygame.display.flip()
            logo_shown = True
    x = random.randint(1, 2)
    if x == 1:
        points += dog_level*0.01
    else:
        pass
    points_surface = points_font.render(f'Squeaks: {int(points)}', True, (0, 0, 0))
    shop_sign = points_font.render(f"Shop", True, (0, 0, 0))
    dog_item = item_font.render(f"Dog (AutoSqueaker): {dog_cost}", True, (0, 0, 0))
    squeaker_item = item_font.render(f"Squeaker Upgrade: {squeaker_cost}", True, (0, 0, 0))
    screen.blit(dog_item, (1250, 200))
    screen.blit(squeaker_item, (1250, 300))
    screen.blit(points_surface, (100, 100))
    screen.blit(shop_sign, (1250, 100))
    screen.blit(squeaker, (500, 250))
    clock.tick(60)
    pygame.display.flip()
