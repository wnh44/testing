import pygame

floor_tile = pygame.image.load("resources/tiles/floor_tile.png")

map = []
for i in range(10):
    map.append([])
    for j in range(20):
        map[i].append("tile")

for i in range(2):
    for j in range(2):
        map[i+4][j+11] = "desk"

for i in range(len(map)):
    print("\n", end="")
    for j in range(len(map[i])):
        print(map[i][j], end=", ")

show = 9

def main(width, height, screen, player_pos):
    # if player_pos[2] >= 5:
    #     show += 1

    for x in range(int(width/floor_tile.get_width()+1)):
        for y in range(int(height/floor_tile.get_height()+1)):
            screen.blit(floor_tile, (x*50, y*50))