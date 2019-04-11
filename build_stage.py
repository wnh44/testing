import pygame

floor_tile = pygame.image.load("resources/tiles/floor_tile.png")


def main(width, height, screen):
    for x in range(int(width/floor_tile.get_width()+1)):
        for y in range(int(height/floor_tile.get_height()+1)):
            screen.blit(floor_tile, (x*50, y*50))