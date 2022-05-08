import pygame
from pygame import Rect


class ImageWrapper:
    def __init__(self, image_path, image_wrapper_id=0):
        self.image_surf = pygame.image.load(image_path).convert_alpha()
        self.image_rect: Rect = self.image_surf.get_rect()
        self.__x, self.__y = 0, 0
        self.image_wrapper_id = image_wrapper_id

    def flip_horizontal(self):
        self.image_surf = pygame.transform.flip(self.image_surf, True, False)

    def blit(self, screen: pygame.Surface):
        screen.blit(self.image_surf, self.image_rect)

    def set_position(self, x, y=None, bottom_left=None):
        if not y:
            y = x[1]
            x = x[0]
        self.__x, self.__y = x, y
        if bottom_left:
            self.__bottomleft(x, y)
        else:
            self.__top_left(x, y)

    def set_x(self, x):
        self.__x = x
        self.image_rect.x = x

    def set_y(self, y):
        self.__y = y
        self.image_rect.y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_position(self):
        return self.__x, self.__y

    def __top_left(self, coordinates, coordinates_b=None):
        try:
            self.image_rect.topleft = coordinates[0], coordinates[1]
        except TypeError:
            self.image_rect.topleft = coordinates, coordinates_b

    def __center(self, coordinates, coordinates_b=None):
        try:
            self.image_rect.center = coordinates[0], coordinates[1]
        except TypeError:
            self.image_rect.center = coordinates, coordinates_b

    def __bottomright(self, coordinates, coordinates_b=None):
        try:
            self.image_rect.bottomright = coordinates[0], coordinates[1]
        except TypeError:
            self.image_rect.bottomright = coordinates, coordinates_b

    def __bottomleft(self, coordinates, coordinates_b=None):
        try:
            self.image_rect.bottomleft = coordinates[0], coordinates[1]
        except TypeError:
            self.image_rect.bottomleft = coordinates, coordinates_b

