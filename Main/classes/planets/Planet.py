import math


class Planet:
    def __init__(self, radius_orb, radius, fi, velocity, colour, centr = None):
        self.radius_orb = radius_orb
        self.radius = radius
        self.fi = fi * 2 * 3.14 / 360
        self.velocity = velocity
        self.colour = colour
        self.center = centr
        self.time = 0
        self.x = self.y = 0

    def move_it_round(self):
        self.time += self.velocity
        if isinstance(self.center, Planet):
            center_x = self.center.x
            center_y = self.center.y
        elif isinstance(self.center, tuple):
            center_x = self.center[0]
            center_y = self.center[1]
        else:
            center_x = center_y = 0
        self.x = int(self.radius_orb * math.sin(self.time + self.fi)) + center_x
        self.y = int(self.radius_orb * math.cos(self.time + self.fi)) + center_y
