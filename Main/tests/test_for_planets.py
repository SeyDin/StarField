import pygame

from Main.classes.planets.Planet import Planet

FPS = 60
WIN_WIDTH = 1920
WIN_HEIGHT = 1050

WHITE = (255, 255, 255)
DARK_BLUE = (0, 0, 10)
ORANGE = (255, 150, 100)
ORANGE2 = (200, 150, 100)
RED = (255, 0, 0)
BLUE = (0, 180, 255)
BLUE2 = (50, 220, 255)
YELLOW = (220, 200, 100)

"""data = {
        'mercury':{'radius':int(0.382*30), 'velocity':int(47.89), 'number':1, 'colour':YELLOW},
          'venus':{'radius':int(0.949*30), 'velocity':int(35.03), 'number':2, 'colour':ORANGE},
          'earth':{'radius':int(1.000*30), 'velocity':int(29.79), 'number':3, 'colour':BLUE},
           'mars':{'radius':int(0.532*30), 'velocity':int(24.13), 'number':4, 'colour':RED},
        'jupiter':{'radius':int(11.209*30), 'velocity':int(13.06), 'number':5, 'colour':ORANGE},
         'saturn':{'radius':int(9.440*30),  'velocity':int(9.640), 'number':6, 'colour':ORANGE2},
           'uran':{'radius':int(4.007*30),  'velocity':int(6.810), 'number':7, 'colour':BLUE2},
         'neptun':{'radius':int(3.883*30),  'velocity':int(5.430), 'number':8, 'colour':BLUE}
         }"""

pygame.init()
clock = pygame.time.Clock()
sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
center = (WIN_WIDTH//2, WIN_HEIGHT//2)

mercury = Planet(150, 10, 0, 0.005, ORANGE, center)
mercury2 = Planet(75, 5, 0, 0.01, BLUE, mercury)
mercury3 = Planet(40, 4, 0, 0.1, RED, mercury2)
mercury4 = Planet(25, 3, 0, 0.12, YELLOW, mercury3)
mercury5 = Planet(150, 3, 0, 0.12, YELLOW, mercury4)

ven = Planet(250, 12, 120, 0.0025, ORANGE, center)
ven2 = Planet(75, 5, 0, 0.01, BLUE, ven)
ven3 = Planet(40, 4, 0, 0.1, RED, ven2)
ven4 = Planet(25, 3, 0, 0.12, YELLOW, ven3)

earth = Planet(350, 12, 240, 0.00125, ORANGE, center)
earth2 = Planet(75, 5, 0, 0.01, BLUE, earth)
earth3 = Planet(40, 4, 0, 0.1, RED, earth2)
earth4 = Planet(25, 3, 0, 0.12, YELLOW, earth3)

ar = [mercury, mercury2, mercury3, mercury4, mercury5, ven, ven2, ven3, ven4, earth, earth2, earth3, earth4]

while True:
    sc.fill(DARK_BLUE)
    for i in pygame.event.get():
        if i.type == pygame.QUIT: exit()
    pygame.draw.circle(sc, YELLOW, (WIN_WIDTH // 2, WIN_HEIGHT // 2), 50)
    clock.tick(FPS)

    for i in ar:
        i.move_it_round()
        pygame.draw.circle(sc, i.colour, (i.x, i.y), i.radius)

    pygame.display.update()
