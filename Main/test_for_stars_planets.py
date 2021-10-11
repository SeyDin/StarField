import pygame

from Main.classes.planets.Planet import Planet
from Main.classes.planets.PlanetsConfigurationResolver import PlanetsConfigurationResolver
from Main.classes.stars.StarsManager import StarsManager

FPS = 60
WIN_WIDTH = 1920
WIN_HEIGHT = 1050

DARK_BLUE = (0, 0, 10)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

stars_manager = StarsManager(500, (0, WIN_WIDTH), (0, WIN_HEIGHT))

center = (WIN_WIDTH//2, WIN_HEIGHT//2)

planets_resolver = PlanetsConfigurationResolver(center)

while True:
    screen.fill(DARK_BLUE)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    clock.tick(FPS)

    stars_manager.calculate_brightness()
    for i in stars_manager.stars:
        pygame.draw.rect(screen, i.color, (i.x, i.y, i.wight, i.wight))
    stars_manager.check_flashes()

    pygame.draw.circle(screen, pygame.color.THECOLORS["orange"], (WIN_WIDTH // 2, WIN_HEIGHT // 2), 50)
    for i in planets_resolver.planets:
        i.move_it_round()
        pygame.draw.circle(screen, i.colour, (i.x, i.y), i.radius)

    pygame.display.update()
