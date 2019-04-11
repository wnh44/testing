import pygame
from build_stage import *

def elevator_level():

    pygame.init()
    font = pygame.font.SysFont("comicsansms", 50)
    text = font.render("Hello, World", True, pygame.Color("red"))

    width, height = 500, 500
    display = pygame.display.set_mode((width, height))
    next_level = None

    while 1:
        display.fill(pygame.Color("white"))
        display.blit(text, ((500 - text.get_width()) // 2, (500 - text.get_height()) // 2))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)