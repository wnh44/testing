import pygame

pygame.init()

blurple = pygame.Color(84, 64, 205)
lighter = pygame.Color(152, 140, 225)
white = pygame.Color("white")
font = pygame.font.Font('resources/fonts/chary.ttf', 24)


def create_dialogue_box(screen, text, by_letter=False, box=True):
    if box:
        pygame.draw.rect(screen, blurple, pygame.Rect(20, 20, 460, 150))
        pygame.draw.rect(screen, lighter, pygame.Rect(25, 25, 450, 140))
    pygame.display.update()
    text_letters = []
    for i in text:
        for j in i:
            text_letters.append(j)
    if by_letter is not False:
        for i in range(by_letter[1]):
            text_object = font.render(text[i], True, white)
            screen.blit(text_object, (40, 40 + 20 * i))
        text_object = font.render(text[by_letter[1]][:by_letter[0]], True, white)
        screen.blit(text_object, (40, 40 + 20 * by_letter[1]))
        if by_letter[0] < len(text[by_letter[1]]) - 1:
            by_letter[0] += 1
        elif by_letter[1] < len(text) - 1:
            by_letter[0] = 0
            by_letter[1] += 1
        pygame.display.update()
        return by_letter
    else:
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