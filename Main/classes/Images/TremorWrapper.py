import time

from classes.Images.ImageWrapper import ImageWrapper


class TremorWrapper:
    def __init__(self, ampl, duration, image_w: ImageWrapper):
        self.ampl = ampl
        self.duration = duration
        self.offset = self.ampl
        self.image_w = image_w
        self.start_time = time.time()
        self.was_state_change = False
        self.was_position_change = False

    def set_position(self, x, y=None):
        self.image_w.set_position(x, y)

    def set_x(self, x):
        self.image_w.set_x(x)

    def set_y(self, y):
        self.image_w.set_y(y)

    def get_x(self):
        return self.image_w.get_x()

    def get_y(self):
        return self.image_w.get_y()

    def calculate_tremor_offset(self, y=True):
        current_time = time.time()
        if current_time - self.start_time > self.duration:
            self.start_time = current_time
            if y:
                self.set_y(self.get_y() + self.offset)
            else:
                self.set_x(self.get_x() + self.offset)
            self.offset = -self.offset


