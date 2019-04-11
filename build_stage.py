import pygame

floor_tile = pygame.image.load("resources/tiles/tile_2.png")
desk_bottom_right = pygame.image.load("resources/tiles/desk_bottom_right.png")
desk_right = pygame.image.load("resources/tiles/desk_right.png")
desk_bottom_left = pygame.image.load("resources/tiles/desk_bottom_left.png")
desk_left = pygame.image.load("resources/tiles/desk_left.png")
desk_bottom = pygame.image.load("resources/tiles/desk_bottom.png")
desk_top = pygame.image.load("resources/tiles/desk_top.png")
desk_top_right = pygame.image.load("resources/tiles/desk_top_right.png")
desk_top_left = pygame.image.load("resources/tiles/desk_top_left.png")
desk_middle = pygame.image.load("resources/tiles/desk_middle.png")
plant = pygame.image.load("resources/images/plant.png")
gloria = pygame.image.load("resources/images/gloria.png")
elevator = pygame.image.load("resources/tiles/elevator.png")


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
    "desk_m": desk_middle,
    "elevator": elevator,
    "none": None
}

stage = []
for x in range(20):
    stage.append([])
    for y in range(10):
        stage[x].append("tile")
stage[5][5] = "desk_bl"
stage[5][4] = "desk_l"
stage[6][5] = "desk_b"
stage[6][4] = "tile"
stage[7][5] = "desk_b"
stage[7][4] = "tile"
stage[8][5] = "desk_br"
stage[8][4] = "desk_r"
stage[14][0] = "elevator"
stage[15][0] = "none"
stage[16][0] = "none"



def build_stage(screen, playerpos):
    # Left edge area
    if playerpos["x"] < 6:
        for x in range(10):
            for y in range(10):
                if translate[stage[x][y]]:
                    screen.blit(translate[stage[x][y]], (x * 50, y * 50))
                if [x, y] == [6, 4]:
                    screen.blit(gloria, (x * 50, y * 50))

    # Right edge area
    elif playerpos["x"] >= 16:
        for x in range(10, 20):
            for y in range(10):
                x_calc = x - 10
                if translate[stage[x][y]]:
                    screen.blit(translate[stage[x][y]], (x_calc * 50, y * 50))
                if [x, y] == [17, 4]:
                    screen.blit(plant, (x_calc * 50, (y - 1) * 50))

    # Middle area
    else:
        for x in range(playerpos["x"] - 5, playerpos["x"] + 5):
            for y in range(10):
                x_calc = x - playerpos["x"] + 5
                if translate[stage[x][y]]:
                    screen.blit(translate[stage[x][y]], (x_calc * 50, y * 50))
                if [x, y] == [17, 4]:
                    screen.blit(plant, (x_calc * 50, (y - 1) * 50))
                if [x, y] == [6, 4]:
                    screen.blit(gloria, (x_calc * 50, y * 50))
