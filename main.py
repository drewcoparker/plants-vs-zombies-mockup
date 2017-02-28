import sys
import pygame
from settings import Settings
from background import Background
import game_functions as gf
from pygame.sprite import Group, groupcollide
from zombie import Zombie
from square import Square



pygame.init()
settings = Settings()
screen = pygame.display.set_mode(settings.screen_size)
pygame.display.set_caption('Plants Vs Zombies Rip-Off')
background = Background(settings)

zombies = Group()
plants = Group()
squares = Group()
bullets = Group()



for i in range(0, 5):
    for j in range(0, 9):
        squares.add(Square(screen, settings, i, j))

def run_game():
    tick = 0
    while 1:
        gf.check_events(screen, settings, squares, plants, bullets)
        gf.update_screen(screen, settings, background, zombies, squares, plants, bullets, tick)
        tick += 1
        if tick % 300 == 0:
            zombies.add(Zombie(screen, settings.zombie_speed, settings.zombie_health))

        pygame.display.flip()


run_game()
