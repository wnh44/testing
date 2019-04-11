import pygame

text_box = pygame.image.load("resources/images/text_box.png")


def create_dialogue_box(screen, text):
    screen.blit(text_box, [0, 0])

    def text_objects(text, font):
        textSurface = font.render(text, True, pygame.Color("black"))
        return textSurface, textSurface.get_rect()

    def message_display(text):
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((500 / 2), (500 / 4))
        screen.blit(TextSurf, TextRect)

        pygame.display.update()

    message_display(text)