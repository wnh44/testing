import pygame
from build_stage import *

def elevator_level(player):

    pygame.init()
    font = pygame.font.SysFont("comicsansms", 50)
    text = font.render("Hello, World", True, pygame.Color("red"))
    elevator_tile = pygame.image.load("resources/tiles/elevator_tile.png")

    playerpos = {
        "xpix": (500 - player.get_width()) // 2,
        "ypix": (500 - player.get_height()) // 2,
        "x": 0,
        "y": 0
    }
    print(playerpos)

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
        # display.blit(elevator_tile, ((500 - elevator_tile.get_width()) // 2, (500 - elevator_tile.get_height()) // 2))
        display.blit(player, ((530 - elevator_tile.get_width()) // 2, (510 - elevator_tile.get_height()) // 2))
        # display.blit(text, ((500 - text.get_width()) // 2, (500 - text.get_height()) // 2))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

# elevator_level()