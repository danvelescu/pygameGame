import pygame

from Screen import Screen


class Player:
    def __init__(self, screen_p, color_p, position_p, round_p):
        self.screen_p = screen_p
        self.color_p = color_p
        self.position_x = position_p[0]
        self.position_y = position_p[1]
        self.round_p = round_p

    def draw(self):
        pygame.draw.circle(self.screen_p, (self.color_p[0], self.color_p[1], self.color_p[2]),
                           (self.position_x, self.position_y), self.round_p)

    def player_key_monitor(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_SPACE] and self.position_y > 0:
            self.position_y -= 4
        else:
            self.position_y += 1

    def track_positon(self):
        if self.position_y > Screen.screen_width:
            self.position_y = Screen.screen_width / 2

