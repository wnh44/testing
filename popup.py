import pygame

pygame.init()

blurple = pygame.Color(84, 64, 205)
lighter = pygame.Color(152, 140, 225)
white = pygame.Color("white")
black = pygame.Color("black")
font = pygame.font.Font('resources/fonts/chary.ttf', 20)


def create_popup(screen, text):
    text_object = font.render(text, True, black)
    text_list = text.split(" ")
    if text_object.get_width() < 440:
        screen.blit(text_object, ((500 - text_object.get_width()) // 2, 475))
    else:
        text_list_2 = []
        string = ""
        for i in text_list:
            if len(string) < 32:
                string = string + i + " "
            else:
                text_list_2.append(string)
                string = i + " "
        text_list_2.append(string)
        for i in range(len(text_list_2)):
            text_object = font.render(text_list_2[i], True, white)
            screen.blit(text_object, ((500 - text_object.get_width()) // 2, 45 + (20 * i)))
    pygame.display.update()