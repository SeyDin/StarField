import pygame

from classes.Images.ImageBeltFactory import ImageBeltFactory
from classes.Images.ImageWrapper import ImageWrapper
from classes.Images.TremorWrapper import TremorWrapper

from classes.resourceHelpers import getPicturePath

FPS = 60
WIN_WIDTH = 1900
WIN_HEIGHT = 1000

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
KRAYOLA = (120, 219, 226)

center_x = WIN_WIDTH // 2
center_y = WIN_HEIGHT // 2

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

car_image = ImageWrapper(getPicturePath("cars/car_1_86_37.png"))
wheel_1_image = ImageWrapper(getPicturePath("misc/wheel_1_15_15.png"))
wheel_2_image = ImageWrapper(getPicturePath("misc/wheel_1_15_15.png"))

car_image_working = TremorWrapper(2, 0.5, car_image)
#way_image_belt = ImageBeltFactory.getImageBelt(getPicturePath("roads/highway_2_32_510.png"), img_num=5, x=0, y=center_y+9, velocity=-3, edge=0)

car_image.set_position((10, center_y))
wheel_1_image.set_position(18, center_y+22)
wheel_2_image.set_position(72, center_y+22)

trees_paths_list = [getPicturePath(f"trees/green_trees_set_{str(x)}.png") for x in range(6)]
trees_image_belt = ImageBeltFactory.getManyImagesBelt(img_paths=trees_paths_list, x=100, y=300, velocity=-3, edge=0, bottom_left=True)


while True:
    screen.fill(KRAYOLA)
    #way_image_belt.blit(screen)
    car_image.blit(screen)
    wheel_1_image.blit(screen)
    wheel_2_image.blit(screen)
    trees_image_belt.blit(screen)

    car_image_working.calculate_tremor_offset()
    #.calculate_images_positions()
    trees_image_belt.calculate_images_positions()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    #car_image.set_position([x + 1 for x in car_image.get_position()])
    #way_image_1.set_x(way_image_1.get_x()-1)
    #car_image.set_y(car_image.get_y()+1)

    pygame.display.update()
    clock.tick(FPS)
