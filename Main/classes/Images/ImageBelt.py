import pygame
from pygame import Rect

from classes.Images.ImageWrapper import ImageWrapper


class ImageBelt:
    def __init__(self, image_w_list: list, velocity: int, edge: int, horizontal: bool = True):
        self.image_w_list = image_w_list
        self.velocity = velocity
        self.edge = edge
        self.horizontal = horizontal

    def replace_image_if_need(self):
        firs_rect: Rect = self.image_w_list[0].image_rect
        last_rect: Rect = self.image_w_list[-1].image_rect
        if self.horizontal:
            first_edge = firs_rect.right
            last_edge = last_rect.right
        else:
            first_edge = firs_rect.top
            last_edge = last_rect.top
        if first_edge <= self.edge:
            self.image_w_list.append(self.image_w_list[0])
            self.image_w_list.pop(0)
            if self.horizontal:
                self.image_w_list[-1].set_x(last_edge)
            else:
                self.image_w_list[-1].set_y(last_edge)
    
    def calculate_images_positions(self):
        self.replace_image_if_need()
        for image_w in self.image_w_list:
            if self.horizontal:
                image_w.set_x(image_w.get_x() + self.velocity)
            else:
                image_w.set_y(image_w.get_y() + self.velocity)

    def blit(self, screen: pygame.Surface):
        for image in self.image_w_list:
            image.blit(screen)
