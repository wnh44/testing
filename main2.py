import pygame
from build_stage import *
from dialogue_box import *

pygame.init()
keypress = False
width, height = 500, 500
keys = {"w": 0, "a": 0, "s": 0, "d": 0}
display = pygame.display.set_mode((width, height))
border = []
for y in range(-1, 11):
    border.append([-1, y])
    border.append([20, y])
for x in range(-1, 21):
    border.append([x, 10])
    border.append([x, -1])
for x in range(5, 7):
    for y in range(4, 6):
        border.append([x, y])
        print(f"{x}, {y}")

player = pygame.image.load("resources/images/caleb_extra_small.png")
playerpos = {
    "xpix": 15, 
    "ypix": (500 - player.get_height()), 
    "x": 0, 
    "y": 9
}
timer = 0


while 1:
    keys = {"w": 0, "a": 0, "s": 0, "d": 0}
    # timer += 1
    if timer >= 800:
        pygame.quit()
        exit(0)
    display.fill(0)
    main(display, playerpos, keypress)
    # create_dialogue_box(screen, "Hello")
    display.blit(player, [playerpos["xpix"], playerpos["ypix"]])
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
        if keys["d"] == 1 and (playerpos["x"] < 6 or 15 < playerpos["x"]):
            # in edge area
            # print("right in edge area, moving")
            playerpos["xpix"] += 50
            playerpos["x"] += 1

        elif keys["d"] == 1:
            # in middle area
            # print("right in middle area, moving")
            playerpos["x"] += 1

    keypress = False
    for i in ['w', 'a', 's', 'd']:
        if keys[i] == 1:
            # if playerpos['x'] in [5, 6]:
            keypress = True
            print(f"player pixels (x, y):  = ({playerpos['xpix']}, {playerpos['ypix']})")
            print(f"player position (x, y):  = ({playerpos['x']}, {playerpos['y']})")
