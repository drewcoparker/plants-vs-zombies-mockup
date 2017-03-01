import pygame

class Settings(object):
    def __init__(self):
        display_info = pygame.display.Info()
        self.screen_size = (display_info.current_w, display_info.current_h)
        self.bg_color = (0, 0, 0)
        self.zombie_speed = 5
        self.zombie_health = 5

        self.squares = {
            'start_left': 368,
            'start_top': 245,
            'square_width': 116,
            'square_height': 102,
            'rows': [
                245,
                347,
                449,
                551,
                653
            ]
        }
        self.highlighted_square = 0
        self.zombie_in_row = [
            0,
            0,
            0,
            0,
            0
        ]
