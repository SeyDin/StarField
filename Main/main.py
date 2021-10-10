import random

import pygame

from Main.classes.Star import Star
from Main.classes.StarsManager import StarsManager

FPS = 60
WIN_WIDTH = 1000
WIN_HEIGHT = 1000

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)

center_x = WIN_WIDTH // 2
center_y = WIN_HEIGHT // 2

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

stars_manager = StarsManager(20, (WIN_HEIGHT//2, WIN_HEIGHT), (WIN_WIDTH//2, WIN_WIDTH))

while True:
    screen.fill(BLACK)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    stars_manager.calculate_brightness()
    for i in stars_manager.stars:
        pygame.draw.rect(screen, i.color, (i.x, i.y, i.wight, i.wight))
    stars_manager.check_flashes()

    pygame.display.update()
    clock.tick(FPS)
