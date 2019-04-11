import pygame

floor_tile = pygame.image.load("resources/tiles/floor_tile.png")
desk_bottom_right = pygame.image.load("resources/tiles/desk_bottom_right.png")
desk_right = pygame.image.load("resources/tiles/desk_right.png")
desk_bottom_left = pygame.image.load("resources/tiles/desk_bottom_left.png")
desk_left = pygame.image.load("resources/tiles/desk_left.png")
desk_bottom = pygame.image.load("resources/tiles/desk_bottom.png")
desk_top = pygame.image.load("resources/tiles/desk_top.png")
desk_top_right = pygame.image.load("resources/tiles/desk_top_right.png")
desk_top_left = pygame.image.load("resources/tiles/desk_top_left.png")
desk_middle = pygame.image.load("resources/tiles/desk_middle.png")


translate = {
    "desk_br": desk_bottom_right,
    "desk_r": desk_right,
    "desk_b": desk_bottom,
    "desk_bl": desk_bottom_left,
    "desk_l": desk_left,
    "desk_t": desk_top,
    "desk_tr": desk_top_right,
    "desk_tl": desk_top_left,
    "tile": floor_tile,
    "desk_m": desk_middle
}

map = []
for x in range(20):
    map.append([])
    for y in range(10):
        map[x].append("tile")
map[5][5] = "desk_bl"
map[5][4] = "desk_l"
map[6][5] = "desk_b"
map[6][4] = "tile"
map[7][5] = "desk_b"
map[7][4] = "tile"
map[8][5] = "desk_br"
map[8][4] = "desk_r"

def main(screen, playerpos, keypress):
    # Left edge area
    if playerpos["x"] <= 5:
        # print("in left edge area")
        for x in range(10):
            if keypress:
                print(f"x: {x}")
            for y in range(10):
                screen.blit(translate[map[x][y]], (x*50, y*50))

    # Right edge area
    elif playerpos["x"] >= 15:
        for x in range(9, 20):
            for y in range(10):
                screen.blit(translate[map[x][y]], ((x-9) * 50, y * 50))

    # Middle area
    else:
        # print("in middle area")
        for x in range(playerpos["x"] - 5, playerpos["x"] + 5):
            if keypress:
                print(f"x: {x}", end=', ')
                print(f"\nx - playerpos[x] + 5 = {x - playerpos['x'] + 5}")
            for y in range(10):
                screen.blit(translate[map[x][y]], ((x - playerpos["x"] + 5) * 50, y * 50))