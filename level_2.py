import pygame
from build_stage import *
# from dialogue_box import *
# from popup import *
from conversation import conversation


def level_2(player):

    pygame.init()
    width, height = 500, 500
    display = pygame.display.set_mode((width, height))
    caleb_speak = False
    caleb_speak_speed = False
    caleb_area = [[6, 5], [6, 3], [5, 4], [7, 4]]
    caleb_text = ["psst... hey", "this is the ice lobby "]
    by_letter = [0, 0]

    border = [[6, 4]]
    into_the_elevator = False
    for y in range(-1, 11):
        border.append([-1, y])
        border.append([11, y])
    for x in range(-1, 15):
        border.append([x, 10])
        border.append([x, 1])

    # stage variables
    stage = []
    for x in range(15):
        stage.append([])
        for y in range(10):
            if y in [0, 1]:
                stage[x].append("wall")
            else:
                stage[x].append("tile")
    stage[6][0] = "elevatorw"
    stage[6][1] = "none"
    stage[7][0] = "none"
    stage[7][1] = "none"

    sprites = [
        [pygame.image.load("resources/images/caleb_extra_small.png"), [6, 4]],
    #     [pygame.image.load("resources/images/plant.png"), [17, 3]]
    ]

    style = {
        "tile": pygame.image.load("resources/tiles/floor_tile_blue_diamond.png"),
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
    timer = 0

    while 1:
        if timer == 1000:
            pygame.quit()
            exit(0)
        keys = {"w": 0, "a": 0, "s": 0, "d": 0}
        display.fill(0)
        build_stage(display, playerpos, stage, style, sprites)
        display.blit(player, [playerpos["xpix"], playerpos["ypix"]])
        caleb_speak, caleb_speak_speed, by_letter = conversation(display, playerpos, caleb_area, caleb_text, by_letter,
                                                                 caleb_speak, caleb_speak_speed)
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
                elif event.key == pygame.K_r:
                    if [playerpos["x"], playerpos["y"]] in caleb_area:
                        if caleb_speak:
                            caleb_speak_speed = True
                        caleb_speak = True
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
        # timer += 1
