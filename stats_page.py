import pygame
from lobby import lobby_level
from elevator import elevator_level

pygame.init()

width, height = 500, 500
display = pygame.display.set_mode((width, height))
next_level = None
font = pygame.font.Font("resources/fonts/astron boy.ttf", 50)
font2 = pygame.font.Font("resources/fonts/astron boy.ttf", 25)

def stats_page():
    text_file = open("player_count.txt", "r")
    player_count_string = text_file.read()
    text_file.close()
    count = []

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
        pygame.image.load("resources/players/caleb.png")
    ]

    for i in range(len(players)):
        if len(player_count_string) > i:
            count.append(int(player_count_string[i]))
        else:
            count.append(0)
    while 1:
        display.fill(pygame.Color(84, 64, 205))
        text = font.render("# of Times Chosen", True, pygame.Color("white"))
        back = font2.render("Back", True, pygame.Color("white"))
        text_rect = text.get_rect()
        text_rect.centerx = display.get_rect().centerx
        text_rect.y = display.get_rect().centery / 4
        display.blit(text, text_rect)
        display.blit(back, (480-back.get_width(), 500-back.get_height()))

        j = 0
        for i in players:
            text = font2.render(str(count[j]), True, pygame.Color("white"))
            text_rect = text.get_rect()
            rect = i.get_rect()
            rect.x = 80 + (70 * (j % 5))
            rect.y = 150 + (90 * (j // 5))
            text_rect.centerx = rect.centerx
            text_rect.y = 205 + (90 * (j // 5))
            display.blit(i, rect)
            display.blit(text, text_rect)
            j += 1

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                pressed = pygame.mouse.get_pressed()
                if pressed[0]:
                    if 480 - back.get_width() < pos[1] < 500:
                        if 500 - back.get_height() < pos[1] < 500:
                            return
