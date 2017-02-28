import pygame
from pygame.sprite import Sprite

class Square(Sprite):
    def __init__(self, screen, settings, i, j):
        super(Square, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.width = settings.squares['square_width']
        self.height = settings.squares['square_height']
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        # our solution:
        # self.rect.top = settings.squares['start_top']
        # self.rect.left = settings.squares['start_left']
        # self.rect.x += (self.rect.width * j)
        # self.rect.y += (self.rect.height * i)
        # print self.rect.y, self.rect.x

        # Rob's solution
        self.rect.left = (j * self.width) + settings.squares['start_left']
        self.rect.top = (i * self.height) + settings.squares['start_top']
        self.square_number = (i * 9) + (j + 1)
        self.row_number = i
        self.column = j
        self.plant_here = False
