import pygame

pygame.init()

blurple = pygame.Color(84, 64, 205)
lighter = pygame.Color(152, 140, 225)
white = pygame.Color("white")
font = pygame.font.Font('resources/fonts/chary.ttf', 24)


def create_dialogue_box(screen, text):
    pygame.draw.rect(screen, blurple, pygame.Rect(20, 20, 460, 150))
    pygame.draw.rect(screen, lighter, pygame.Rect(25, 25, 450, 140))
    text_object = font.render(text, True, white)
    text_list = text.split(" ")
    if text_object.get_width() < 440:
        screen.blit(text_object, ((500 - text_object.get_width()) // 2, 80))
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