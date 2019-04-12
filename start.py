import pygame
from player_select import player_select
from lobby import lobby_level
from elevator import elevator_level
from level_2 import level_2
from stats_page import stats_page

pygame.init()

width, height = 500, 500
display = pygame.display.set_mode((width, height))
next_level = None
font = pygame.font.Font("resources/fonts/astron boy.ttf", 50)
font2 = pygame.font.Font("resources/fonts/astron boy.ttf", 35)

while 1:
    display.fill(pygame.Color(84, 64, 205))
    text = font.render("Welcome to Adtran!", True, pygame.Color("white"))
    text2 = font2.render("Press Enter to get started", False, pygame.Color("white"))
    text_rects = [text.get_rect(), text2.get_rect()]
    text_rects[0].centerx, text_rects[1].centerx = display.get_rect().centerx, display.get_rect().centerx
    text_rects[0].y = display.get_rect().centery/2
    text_rects[1].y = display.get_rect().centery * (3/2)
    display.blit(text, text_rects[0])
    display.blit(text2, text_rects[1])
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                player = player_select()
                while player == "Stats Page":
                    stats_page()
                    player = player_select()
                next_level = "Lobby"
    if next_level:
        break

while 1:
    if next_level == "Elevator":
        next_level = elevator_level(player)
    elif next_level == "Lobby":
        next_level  = lobby_level(player)
    elif next_level == "2":
        next_level = level_2(player)
    elif next_level == "3":
        pass