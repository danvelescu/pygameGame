import pygame

from Player import Player
from Screen import ScreenResolution
from Utils import Barrier

pygame.init()

ScreenResolution.screen_height = 600
ScreenResolution.screen_width = 800

screen = pygame.display.set_mode([ScreenResolution.screen_width, ScreenResolution.screen_height])

player = Player(screen, (10, 228, 124), (70, 250), 20)
barrier_top_1 = Barrier((100, 100), (100, 100, 100), screen,
                 (ScreenResolution.screen_width / 5, ScreenResolution.screen_height / 3))  # position, color, screen, rect
barrier_top_2 = Barrier((100, 100), (100, 100, 100), screen,
                 (ScreenResolution.screen_width / 5, ScreenResolution.screen_height / 3))
barrier_bottom_1 = Barrier((100, 100), (100, 100, 100), screen,
                 (ScreenResolution.screen_width / 5, ScreenResolution.screen_height / 3))
barrier_bottom_2 = Barrier((100, 100), (100, 100, 100), screen,
                 (ScreenResolution.screen_width / 5, ScreenResolution.screen_height / 3))

barrier_top_1.pin_to_start_position_top()
barrier_top_1.rect.x += 300
barrier_top_2.pin_to_start_position_top()

barrier_bottom_1.pin_to_start_position_bottom()
barrier_bottom_1.rect.x += 300
barrier_bottom_2.pin_to_start_position_bottom()



clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    screen.fill((225, 245, 244))
    player.draw()

    barrier_top_1.draw()
    barrier_top_1.barrier_move()

    barrier_top_2.draw()
    barrier_top_2.barrier_move()

    barrier_bottom_1.draw()
    barrier_bottom_1.barrier_move()

    barrier_bottom_2.draw()
    barrier_bottom_2.barrier_move()


    player.track_positon()
    player.player_key_monitor()

    pygame.display.flip()
    clock.tick(60)
