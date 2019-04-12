import pygame
from build_stage import *

def elevator_level():

    pygame.init()
    font = pygame.font.SysFont("comicsansms", 50)
    text = font.render("Hello, World", True, pygame.Color("red"))
    elevator_tile = pygame.image.load("resources/images/elevator_tile.png")
    player = pygame.image.load("resources/images/caleb_extra_small.png")

    playerpos = [((500 - player.get_width()) // 2, (500 - player.get_height()) // 2)]
    print(playerpos)

    width, height = 500, 500
    display = pygame.display.set_mode((width, height))
    next_level = None

    while 1:
        display.fill(pygame.Color("black"))
        display.blit(elevator_tile, ((500 - elevator_tile.get_width()) // 2, (500 - elevator_tile.get_height()) // 2))
        display.blit(player, ((530 - elevator_tile.get_width()) // 2, (510 - elevator_tile.get_height()) // 2))
        # display.blit(text, ((500 - text.get_width()) // 2, (500 - text.get_height()) // 2))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

# elevator_level()