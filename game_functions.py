import sys
import pygame
from plant import Plant
from peashooter import Peashooter
from bullet import Bullet


def check_events(screen, settings, squares, plants, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for square in squares:
                if square.rect.collidepoint(mouse_x, mouse_y):
                    print "Square: ", square.square_number
                    plants.add(Peashooter(screen, square))


def update_screen(screen, settings, background, zombies, squares, plants, bullets, tick):
    screen.blit(background.image, background.rect)

    for zombie in zombies.sprites():
        zombie.update_me()
        zombie.draw_me()

    for plant in plants:
        plant.draw_me()
        if tick % 30 == 0:
            bullets.add(Bullet(screen, plant))

    for bullet in bullets.sprites():
        bullet.update_me(plant)
        bullet.draw_me()
