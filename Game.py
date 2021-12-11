import pygame

from Player import Player
from Screen import Screen
from Utils import Barrier

pygame.init()

Screen.screen_height = 500
Screen.screen_width = 500

screen = pygame.display.set_mode([Screen.screen_width, Screen.screen_height])

player = Player(screen, (10, 228, 124), (70, 250), 20)
barier = Barrier((100, 100), (100, 100, 100), screen,
                 (Screen.screen_width / 5, Screen.screen_height / 3))  # position, color, screen, rect

barier.pin_to_start_position()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    screen.fill((225, 245, 244))
    player.draw()
    barier.draw()
    player.track_positon()
    player.player_key_monitor()
    pygame.display.flip()
    clock.tick(60)
