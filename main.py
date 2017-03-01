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
        if tick % 110 == 0 or tick == 1:
            zombies.add(Zombie(screen, settings))

        zombies_hit = groupcollide(zombies, bullets, False, False)
        plant_got_hit = groupcollide(plants, zombies, True, False)
        for zombie in zombies_hit:
            print zombie
            print zombies_hit
            if zombie.yard_row == zombies_hit[zombie][0].yard_row:
                bullets.remove(zombies_hit[zombie][0])
                zombie.hit(1)
                if zombie.health <= 0:
                    zombies.remove(zombie)
                    settings.zombie_in_row[zombie.yard_row] -= 1

        pygame.display.flip()


run_game()
