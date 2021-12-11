import pygame


class Barrier:
    def __init__(self, position, color, screen, rect):
        self.position = position
        self.color = color
        self.screen = screen
        self.rect = pygame.Rect(position[0], position[1], rect[0], rect[1])

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def pin_to_start_position(self):
        self.rect.x = 400
        self.rect.y = 0
