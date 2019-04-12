import pygame
from lobby import lobby_level
from elevator import elevator_level

pygame.init()

width, height = 500, 500
display = pygame.display.set_mode((width, height))
next_level = None
font = pygame.font.Font("resources/fonts/astron boy.ttf", 50)
font2 = pygame.font.Font("resources/fonts/astron boy.ttf", 25)

def player_select():
    text_file = open("player_count.txt", "r")
    player_count_string = text_file.read()
    text_file.close()
    text_file_write = open("player_count.txt", "w")
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
        text = font.render("Choose your character", True, pygame.Color("white"))
        stats_text = font2.render("Player Stats", True, pygame.Color("white"))
        text_rect = text.get_rect()
        text_rect.centerx = display.get_rect().centerx
        text_rect.y = display.get_rect().centery / 4
        display.blit(text, text_rect)
        display.blit(stats_text, (480-stats_text.get_width(), 500-stats_text.get_height()))

        j = 0
        for i in players:
            display.blit(i, (80 + (70 * (j % 5)), 150 + (60 * (j // 5))))
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
                    if 150 < pos[1] < 200:
                        j = 0
                        for i in players[:5]:
                            if 80 + (j * 70) < pos[0] < 130 + (j * 70):
                                string = ""
                                count[j] += 1
                                for k in count:
                                    string += (str(k))
                                text_file_write.write(string)
                                text_file_write.close()
                                return i
                            j += 1
                    elif 210 < pos[1] < 260:
                        j = 0
                        for i in players[5:]:
                            if 80 + (j * 70) < pos[0] < 130 + (j * 70):
                                string = ""
                                count[j+5] += 1
                                for k in count:
                                    string += (str(k))
                                text_file_write.write(string)
                                text_file_write.close()
                                return i
                            j += 1
                    elif 270 < pos[1] < 320:
                        j = 0
                        for i in players[10:]:
                            if 80 + (j * 70) < pos[0] < 130 + (j * 70):
                                string = ""
                                count[j+10] += 1
                                for k in count:
                                    string += (str(k))
                                text_file_write.write(string)
                                text_file_write.close()
                                return i
                            j += 1
                    elif 480 - stats_text.get_width() < pos[1] < 500:
                        if 500 - stats_text.get_height() < pos[1] < 500:
                            string = ""
                            for k in count:
                                string += str(k)
                            text_file_write.write(string)
                            text_file_write.close()
                            return "Stats Page"
