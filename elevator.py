import pygame
from build_stage import *
import dialogue_box


def elevator_level(player):
    pygame.init()
    font = pygame.font.SysFont("comicsansms", 50)
    text = font.render("Hello, World", True, pygame.Color("red"))
    elevator_tile = pygame.image.load("resources/tiles/elevator_tile.png")

    playerpos = {
        "xpix": 300,
        "ypix": 300,
        "x": 0,
        "y": 0
    }
    # print(playerpos)

    width, height = 500, 500
    display = pygame.display.set_mode((width, height))
    next_level = None

    stage = []
    for x in range(7):
        stage.append([])
        for y in range(7):
            if y > 3 and x > 3:
                stage[x].append("floor")
            else:
                stage[x].append("none")

    style = {
        "floor": elevator_tile,
        "none": None
    }

    sprites = [
        [pygame.image.load("resources/sprites/elevator_buttons.png"), [4, 6]]
    ]

    while 1:
        display.fill(pygame.Color("black"))
        build_stage(display, playerpos, stage, style, sprites)
        display.blit(player, ((550 - elevator_tile.get_width()) // 2, (550 - elevator_tile.get_height()) // 2))
        dialogue_box.create_dialogue_box(display, "1: Lobby   2: Ice   3: Desert", False, False)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    next_level = "2"
                # elif event.key == pygame.K_3:
                #     next_level = "3"
        if next_level is not None:
            return next_level
