import pygame
from Screen import ScreenResolution

class Barrier:
    def __init__(self, position, color, screen, rect):
        self.position = position
        self.color = color
        self.screen = screen
        self.rect = pygame.Rect(position[0], position[1], rect[0], rect[1])

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def pin_to_start_position_top(self):
        self.rect.x = ScreenResolution.screen_width
        self.rect.y = 0

    def pin_to_start_position_bottom(self):
        self.rect.x = ScreenResolution.screen_width
        self.rect.y = ScreenResolution.screen_height - 100

    def pin_to_start_position_X(self):
        self.rect.x = ScreenResolution.screen_width

    def barrier_move(self):
        if -ScreenResolution.screen_width / 3 > self.rect.x:
            self.pin_to_start_position_X()
        self.rect.x += -2
