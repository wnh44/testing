import pygame
from build_stage import *
from dialogue_box import *

pygame.init()
width, height = 500, 500
keys = [0, 0, 0, 0]
screen = pygame.display.set_mode((width, height))

player = pygame.image.load("resources/images/caleb_extra_small.png")
playerpos = [15, (500 - player.get_height()), 0, 9]
timer = 0


while 1:
    keys = [0, 0, 0, 0]
    # timer += 1
    if timer >= 500:
        pygame.quit()
        exit(0)
    screen.fill(0)
    main(width, height, screen)
    # create_dialogue_box(screen, "Hello")
    screen.blit(player, playerpos)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                keys[0] = 1
            elif event.key == pygame.K_a and keys[1] is 0:
                keys[1] = 1
            elif event.key == pygame.K_s and keys[2] is 0:
                keys[2] = 1
            elif event.key == pygame.K_d and keys[3] is 0:
                keys[3] = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = 0
            elif event.key == pygame.K_a and keys[1] is 1:
                keys[1] = 0
            elif event.key == pygame.K_s and keys[2] is 1:
                keys[2] = 0
            elif event.key == pygame.K_d and keys[3] is 1:
                keys[3] = 0
    if keys[0] == 1 and playerpos[3] > 0:
        playerpos[1] -= 50
        playerpos[3] -= 1
    elif keys[2] == 1 and playerpos[3] < 9:
        playerpos[1] += 50
        playerpos[3] += 1
    if keys[1] == 1 and playerpos[2] > 0:
        playerpos[0] -= 50
        playerpos[2] -= 1
    elif keys[3] == 1 and playerpos[2] < 19:
        playerpos[0] += 50
        playerpos[2] += 1
