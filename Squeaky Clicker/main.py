#Import Necessary Libraries
import os
import pygame
import random
import time
import json

#Init pygame modules such as clock, mixer, etc.
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
running = True
#Initialize the screen
screen = pygame.display.set_mode((1080, 1920), pygame.FULLSCREEN)
pygame.display.set_caption('Squeaky Clicker - Made For Cuprum')
center_h = 300
center_w = 0
squeaker_level = 1
points = 0
dog_level = 0
#Attempt to load save data
try:
    with open("./saves/save.json", "r") as f:
        save = json.load(f)
        points = save["points"]
        dog_level = save["dog_level"]
        squeaker_level = save["squeaky"]
except FileNotFoundError:
#If its unable to be loaded, just go with the defualt.
    pass
logo_shown = False
menu_shown = False
screen.fill((0, 0, 0))
pygame.display.flip()
#Load the squeaky
squeaker = pygame.image.load(f'./assets/squeakers/squeaky1.png')
pygame.display.set_icon(pygame.image.load(f'./assets/branding/Logo1.png'))
#FONTS
points_font = pygame.font.SysFont('Comic Sans MS', 50)
item_font = pygame.font.SysFont('Comic Sans MS', 30)
floaty_point_text = pygame.font.SysFont('Comic Sans MS', 25, bold=True)
menu_header = points_font
additional_number = random.randint(1, 10)
#Main Game LooLoop
while running:
    dog_cost = dog_level+1
    dog_cost *= 35
    dog_cost **= 1.5
    dog_cost += additional_number
    dog_cost = int(dog_cost)
    squeaker_cost = squeaker_level*2
    squeaker_cost **= 1.5
    squeaker_cost += additional_number
    squeaker_cost = int(squeaker_cost)
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if os.path.exists("./saves/save.json"):
                with open("./saves/save.json", "w") as f:
                    data = {
                        "squeaky": squeaker_level,
                        "points": int(points),
                        "dog_level": dog_level,
                    }
                    json.dump(data, f, indent=4)
            else:
                try:
                    os.mkdir("./saves")
                except:
                    pass
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                points_tobeadded = 1*squeaker_level
                points += points_tobeadded
                squeak = pygame.mixer.Sound('./assets/squeakers/squeak.wav')
                squeak.play()
                floaty_point_text_text = floaty_point_text.render(f"+{points_tobeadded}", True, (0, 0, 0))
                screen.blit(floaty_point_text_text, (400, 100))
            if event.key == pygame.K_0:
                #Yes i know this is a bad name ill change it later.
                tmpvar = squeaker_level *20
                points_toberemoved = tmpvar**1.5
                if int(points) >= points_toberemoved:
                    print(f"Points: {points}, Points to be removed: {points_toberemoved}")
                    squeaker_level += 1
                    print(points_toberemoved)
                    points -= points_toberemoved+additional_number
                    additional_number = random.randint(1, 10)
                else:
                    print("Not Enough Squeaks to purchase this upgrade!")
            if event.key == pygame.K_1:
                points_toberemoved = dog_level+1
                points_toberemoved *= 35
                points_toberemoved **= 1.5
                if int(points) >= points_toberemoved:
                    dog_level += 1
                    print(points_toberemoved)
                    points -= points_toberemoved+additional_number
                    additional_number = random.randint(1, 10)
                else:
                    print("Not Enough Squeaks to purchase this upgrade!")
    if not logo_shown:
        for i in range(255):
            for event in pygame.event.get():
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
            screen.fill((i, i, i))
            time.sleep(0.007)
            pygame.display.flip()
        for i in range(75):
            for event in pygame.event.get():
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
            screen.fill((255, 255, 255))
            x = random.randint(1, 3)
            logo = pygame.image.load(f'./assets/branding/Logo{x}.png')
            screen.blit(logo, (center_h, center_w))
            pygame.display.flip()
            time.sleep(0.02)
        for i in range(255):
            for event in pygame.event.get():
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
            screen.fill((255-i, 255-i, 255-i))
            time.sleep(0.007)
            pygame.display.flip()
            logo_shown = True
    if not menu_shown:
        squeaked = False
        while not squeaked:
            header = menu_header.render(f"Squeaky Clicker", True, (255, 255, 255))
            screen.blit(header, (500, 100))
            playtext = menu_header.render(f"Squeak to begin...", True, (255, 255, 255))
            reset_text = menu_header.render(f"Press down on 1 to reset save data", True, (255, 255, 255))
            screen.blit(playtext, (500, 200))
            screen.blit(reset_text, (500, 300))
            pygame.display.flip()
            for event in pygame.event.get():
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        squeaked = True
                        menu_shown = True
                    if event.key == pygame.K_1:
                        os.remove("./saves/save.json")
                        squeaked = True
                        menu_shown = True
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
