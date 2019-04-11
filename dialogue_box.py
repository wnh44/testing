import pygame

text_box = pygame.image.load("resources/images/text_box.png")


def create_dialogue_box(screen, text):
    screen.blit(text_box, ((500 - text_box.get_width()) // 2, 5))
    font = pygame.font.Font('freesansbold.ttf', 20)
    text_object = font.render(text, True, pygame.Color("black"))
    screen.blit(text_object, ((500 - text_object.get_width()) // 2, 80))
    pygame.display.update()