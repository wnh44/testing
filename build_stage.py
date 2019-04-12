

def build_stage_sprites(playerpos, stage_size, screen, sprites):

    # Left edge area
    if playerpos["x"] < 6:
        for x in range(10):
            for y in range(10):
                for i in sprites:
                    if [x, y] == i[1]:
                        screen.blit(i[0], (x * 50, y * 50))

    # Right edge area
    elif playerpos["x"] >= stage_size["x"] - 4:
        for x in range(stage_size["x"] - 10, stage_size["x"]):
            for y in range(10):
                x_calc = x - 10
                for i in sprites:
                    if [x, y] == i[1]:
                        screen.blit(i[0], (x_calc * 50, y * 50))

    # Middle area
    else:
        for x in range(playerpos["x"] - 5, playerpos["x"] + 5):
            for y in range(10):
                x_calc = x - playerpos["x"] + 5
                for i in sprites:
                    if [x, y] == i[1]:
                        screen.blit(i[0], (x_calc * 50, y * 50))


def build_stage(screen, playerpos, stage, style, sprites):
    stage_size = {
        "x": len(stage),
        "y": len(stage[0])
    }

    # Left edge area
    if playerpos["x"] < 6:
        for x in range(10):
            for y in range(10):
                if style[stage[x][y]]:
                    screen.blit(style[stage[x][y]], (x * 50, y * 50))

    # Right edge area
    elif playerpos["x"] >= stage_size["x"] - 4:
        for x in range(stage_size["x"] - 10, stage_size["x"]):
            for y in range(10):
                x_calc = x - 10
                if style[stage[x][y]]:
                    screen.blit(style[stage[x][y]], (x_calc * 50, y * 50))

    # Middle area
    else:
        for x in range(playerpos["x"] - 5, playerpos["x"] + 5):
            for y in range(10):
                x_calc = x - playerpos["x"] + 5
                if style[stage[x][y]]:
                    screen.blit(style[stage[x][y]], (x_calc * 50, y * 50))

    build_stage_sprites(playerpos, stage_size, screen, sprites)
