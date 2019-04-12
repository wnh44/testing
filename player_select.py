import pygame
from lobby import lobby_level
from elevator import elevator_level

pygame.init()

width, height = 500, 500
display = pygame.display.set_mode((width, height))
next_level = None
font = pygame.font.Font("resources/fonts/astron boy.ttf", 50)
font2 = pygame.font.Font("resources/fonts/astron boy.ttf", 35)

def player_select():
    players = [
        pygame.image.load("resources/players/blake.png"),
        pygame.image.load("resources/players/jacob.png"),
        pygame.image.load("resources/players/pranay.png"),
        pygame.image.load("resources/players/scott.png"),
        pygame.image.load("resources/players/krysten.png"),
        pygame.image.load("resources/players/brittany.png"),
        pygame.image.load("resources/players/jake.png"),
        pygame.image.load("resources/players/joenid.png"),
        pygame.image.load("resources/players/luke.png"),
        pygame.image.load("resources/players/nick.png"),
        pygame.image.load("resources/players/will.png"),
    ]

    while 1:
        display.fill(pygame.Color(84, 64, 205))
        text = font.render("Choose your character", True, pygame.Color("white"))
        text_rect = text.get_rect()
        text_rect.centerx = display.get_rect().centerx
        text_rect.y = display.get_rect().centery / 2
        display.blit(text, text_rect)

        j = 0
        for i in players:
            display.blit(i, (80 + (70 * (j % 5)), 280 + (60 * (j // 5))))
            j += 1

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                pressed = pygame.mouse.get_pressed()
                if pressed[0]:
                    if 280 < pos[1] < 330:
                        j = 0
                        for i in players[:5]:
                            if 80 + (j * 70) < pos[0] < 130 + (j * 70):
                                return i
                            j += 1
                    elif 340 < pos[1] < 390:
                        j = 0
                        for i in players[5:]:
                            if 80 + (j * 70) < pos[0] < 130 + (j * 70):
                                return i
                            j += 1
                    elif 400 < pos[1] < 450:
                        j = 0
                        for i in players[10:]:
                            if 80 + (j * 70) < pos[0] < 130 + (j * 70):
                                return i
                            j += 1
