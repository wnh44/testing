import pygame
from build_stage import *
from dialogue_box import *
from popup import *


def lobby_level(player):

    pygame.init()
    width, height = 500, 500
    display = pygame.display.set_mode((width, height))

    border = [[5, 4], [8, 4], [17, 4], [17, 3], [6, 4]]
    gloria_speak = False
    by_letter = [0, 0]
    into_the_elevator = False
    for y in range(-1, 11):
        border.append([-1, y])
        border.append([20, y])
    for x in range(-1, 21):
        border.append([x, 10])
        border.append([x, 1])
    for x in range(5, 9):
        border.append([x, 5])

    # stage variables
    stage = []
    for x in range(20):
        stage.append([])
        for y in range(10):
            if y in [0, 1]:
                stage[x].append("wall")
            else:
                stage[x].append("tile")
    stage[5][5] = "desk_bl"
    stage[5][4] = "desk_l"
    stage[6][5] = "desk_b"
    stage[6][4] = "tile"
    stage[7][5] = "desk_b"
    stage[7][4] = "tile"
    stage[8][5] = "desk_br"
    stage[8][4] = "desk_r"
    stage[14][0] = "elevatorw"
    stage[14][1] = "none"
    stage[15][0] = "none"
    stage[15][1] = "none"
    stage[2][0] = "windowl"
    stage[2][1] = "none"
    stage[3][0] = "windowr"
    stage[3][1] = "none"
    stage[8][0] = "windowl"
    stage[8][1] = "none"
    stage[9][0] = "windowr"
    stage[9][1] = "none"

    sprites = [
        [pygame.image.load("resources/images/gloria.png"), [6, 4]],
        [pygame.image.load("resources/images/plant.png"), [17, 3]]
    ]

    style = {
        "desk_br": pygame.image.load("resources/tiles/desk_bottom_right.png"),
        "desk_r": pygame.image.load("resources/tiles/desk_right.png"),
        "desk_b": pygame.image.load("resources/tiles/desk_bottom.png"),
        "desk_bl": pygame.image.load("resources/tiles/desk_bottom_left.png"),
        "desk_l": pygame.image.load("resources/tiles/desk_left.png"),
        "desk_t": pygame.image.load("resources/tiles/desk_top.png"),
        "desk_tr": pygame.image.load("resources/tiles/desk_top_right.png"),
        "desk_tl": pygame.image.load("resources/tiles/desk_top_left.png"),
        "tile": pygame.image.load("resources/tiles/tile_2.png"),
        "desk_m": pygame.image.load("resources/tiles/desk_middle.png"),
        "elevator": pygame.image.load("resources/tiles/elevator.png"),
        "none": None,
        "wall": pygame.image.load("resources/tiles/wall_tile.png"),
        "windowr": pygame.image.load("resources/tiles/window_right.png"),
        "windowl": pygame.image.load("resources/tiles/window_left.png"),
        "elevatorw": pygame.image.load("resources/tiles/elevator_wall.png")
    }

    playerpos = {
        "xpix": 50 / player.get_width(),
        "ypix": (500 - player.get_height()),
        "x": 0,
        "y": 9
    }
    gloria_talked = False

    while 1:
        keys = {"w": 0, "a": 0, "s": 0, "d": 0}
        display.fill(0)
        build_stage(display, playerpos, stage, style, sprites)
        display.blit(player, [playerpos["xpix"], playerpos["ypix"]])

        # Gloria conversation
        if (playerpos["x"] == 6 and playerpos["y"] in [6, 3]) or (playerpos["x"] == 7 and playerpos["y"] in [6, 4]):
            if gloria_speak:
                by_letter = create_dialogue_box(display, ["Hi! My name is Gloria. Welcome to",
                                                          "Adtran! We've got a lot for you to get",
                                                          "started on, so go ahead and head to",
                                                          "the elevator on your right. "], by_letter)
                # create_dialogue_box(display, "Hi! My name is Gloria. Welcome to Adtran! We've got a lot for you to get "
                #                              "started on, so go ahead and head to the elevator on your right.")
            else:
                create_popup(display, "Press R to Speak")
        else:
            gloria_speak = False
            by_letter = [0, 0]


        if playerpos["x"] in [14, 15] and playerpos["y"] == 2:
            if gloria_talked:
                create_popup(display, "Press Spacebar to Enter Elevator")
            else:
                create_popup(display, "Adtran badge needed")

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    keys["w"] = 1
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    keys["a"] = 1
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    keys["s"] = 1
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    keys["d"] = 1
                elif event.key == pygame.K_SPACE and playerpos["x"] in [14, 15] and playerpos["y"] == 2 and gloria_talked is True:
                    into_the_elevator = True
                elif event.key == pygame.K_r and (playerpos["x"] == 6 and playerpos["y"] == 6) or (playerpos["x"] == 6 and playerpos["y"] == 3) or (playerpos["x"] == 7 and playerpos["y"] == 6) or (playerpos["x"] == 7 and playerpos["y"] == 4):
                    gloria_speak = True
                    gloria_talked = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    keys["w"] = 0
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    keys["a"] = 0
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    keys["s"] = 0
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    keys["d"] = 0

        #UP
        if keys["w"] == 1 and [playerpos["x"], playerpos["y"] - 1] not in border:
            playerpos["ypix"] -= 50
            playerpos["y"] -= 1

        #DOWN
        if keys["s"] == 1 and [playerpos["x"], playerpos["y"] + 1] not in border:
            playerpos["ypix"] += 50
            playerpos["y"] += 1

        #LEFT
        if [playerpos["x"] - 1, playerpos["y"]] not in border:
            if keys["a"] == 1 and (playerpos["x"] < 6 or 15 < playerpos["x"]):
                # in edge area
                playerpos["xpix"] -= 50
                playerpos["x"] -= 1

            elif keys["a"] == 1:
                # in middle area
                playerpos["x"] -= 1

        #RIGHT
        if [playerpos["x"] + 1, playerpos["y"]] not in border:
            if keys["d"] == 1 and (playerpos["x"] < 5 or 14 < playerpos["x"]):
                # in edge area
                playerpos["xpix"] += 50
                playerpos["x"] += 1

            elif keys["d"] == 1:
                # in middle area
                playerpos["x"] += 1

        for i in ['w', 'a', 's', 'd']:
            if keys[i] == 1:
                print(f"player position (x, y):  = ({playerpos['x']}, {playerpos['y']})")

        if into_the_elevator:
            return "Elevator"
