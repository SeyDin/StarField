from Main.classes.stars.Star import Star
import random


class StarsManager:
    def __init__(self, num, range_x, range_y, range_dif=(1, 10), range_size=(1, 3), randomise=True, flashable=True):
        self.num = num
        self.stars = []
        self.min_x = range_x[0]
        self.max_x = range_x[1]
        self.min_y = range_y[0]
        self.max_y = range_y[1]
        self.min_dif = range_dif[0]
        self.max_dif = range_dif[1]
        self.min_size = range_size[0]
        self.max_size = range_size[1]
        self.randomise = randomise
        self.flashable = flashable
        if self.randomise:
            self.__random_generate()

    def __random_generate(self):
        self.stars = []
        for i in range(self.num):
            self.add_random_star()

    def calculate_brightness(self):
        for star in self.stars:
            star.calculate_brightness()

    def check_flashes(self):
        died = []
        for i in self.stars:
            if i.flash:
                died.append(i)
        for i in died:
            self.stars.remove(i)
            self.add_random_star()
        died.clear()

    def add_random_star(self):
        self.stars.append(Star(random.randint(self.min_x, self.max_x),
                               random.randint(self.min_y, self.max_y),
                               random.randint(self.min_size, self.max_size + 1),
                               random.randint(self.min_dif, self.max_dif))
                          )
