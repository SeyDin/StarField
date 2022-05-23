import random

import pygame
from pygame import Rect


class ImageBelt:
    def __init__(self, image_w_list: list, velocity: int, edge: int, shift=0, shift_random=False, shaking_random=0, flip_random=False, horizontal: bool = True):
        self.image_w_list = image_w_list
        self.velocity = velocity
        self.edge = edge
        self.horizontal = horizontal
        self.shift = shift
        self.shift_random = shift_random
        self.shaking_random = shaking_random
        self.flip_random = flip_random

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
            r_shift = self.shift
            if self.shift_random:
                r_shift = random.randint(self.shift - self.shift//2, self.shift + self.shift//2)
            r_shaking_random = 0
            if self.shaking_random:
                r_shaking_random = random.randint(0, self.shaking_random)
            r_flip = False
            if self.flip_random:
                r_flip = bool(random.getrandbits(1))
            if self.horizontal:
                self.image_w_list[-1].set_x(last_edge - r_shift)
                self.image_w_list[-1].flip(r_flip, False)
            else:
                self.image_w_list[-1].set_y(last_edge - r_shift)
                self.image_w_list[-1].flip(False, r_flip)
    
    def calculate_images_positions(self):
        self.replace_image_if_need()
        for image_w in self.image_w_list:
            if self.horizontal:
                image_w.set_x(image_w.get_x() + self.velocity)
                # print(image_w.image_wrapper_id, image_w.get_x(), image_w.get_y())
            else:
                image_w.set_y(image_w.get_y() + self.velocity)

    def blit(self, screen: pygame.Surface):
        for image in self.image_w_list:
            image.blit(screen)
