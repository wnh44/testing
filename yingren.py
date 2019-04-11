import pygame, math, random
from pygame.locals import *

pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

keys = [False, False, False, False]
playerpos = [100, 100]
bodypos = [0, 0]

player = pygame.image.load("resources/images/caleb_with_body.png")
background = pygame.image.load("resources/images/adtran.jpg")

while 1:
    screen.fill(0)
    screen.blit(background, [0,0])
    screen.blit(player, playerpos)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                keys[0] = True
            elif event.key == pygame.K_a:
                keys[1] = True
            elif event.key == pygame.K_s:
                keys[2] = True
            elif event.key == pygame.K_d:
                keys[3] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            elif event.key == pygame.K_a:
                keys[1] = False
            elif event.key == pygame.K_s:
                keys[2] = False
            elif event.key == pygame.K_d:
                keys[3] = False
    if keys[0] and playerpos[1] > 0:
        playerpos[1] -= 5
    elif keys[2] and playerpos[1] < (480 - player.get_height()):
        playerpos[1] += 5
    if keys[1] and playerpos[0] > 0:
        playerpos[0] -= 5
    elif keys[3] and playerpos[0] < (640 - player.get_width()):
        playerpos[0] += 5
