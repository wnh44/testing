import pygame
from main2 import main
from elevator import elevator_level

pygame.init()

width, height = 500, 500
display = pygame.display.set_mode((width, height))
next_level = None

while 1:
    display.fill(pygame.Color("dodgerblue"))
    font = pygame.font.Font(None, 50)
    font2 = pygame.font.Font(None, 30)
    text = font.render("Welcome to Adtran!", True, pygame.Color("white"))
    text2 = font2.render("Press Enter to get started", True, pygame.Color("white"))
    display.blit(text, ((500 - text.get_width()) // 2, (500 - text.get_height()) // 2))
    display.blit(text2, (((500 - text2.get_width()) // 2), ((500 - text2.get_height()) // 2) + 100))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                next_level = main()
    if next_level:
        break

if next_level == "Elevator":
    next_level = elevator_level()