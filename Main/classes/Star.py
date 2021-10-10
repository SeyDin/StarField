class Star:
    def __init__(self, x, y, wight, diff=1):
        self.x = x
        self.y = y
        self.wight = wight
        self.diff = diff if diff > 0 else 1
        self.frame = 0
        self.brightness = 1
        self.color = [self.brightness,
                      self.brightness,
                      self.brightness]
        self.flash = False

    def calculate_brightness(self):
        self.brightness += self.diff
        if self.brightness >= 255:
            self.diff *= -1
            self.brightness = 255
        elif self.brightness <= 0:
            self.diff *= -1
            self.brightness = 0
            self.flash = True
        self.color = [self.brightness for i in self.color]
