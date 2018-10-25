class Turret:
    def __init__(self, x_pin: int, y_pin: int, laser_pin: int,
                 x_center: int, y_center: int,
                 x_offset: int =0, y_offset: int =0):
        self.x_pin = x_pin
        self.y_pin = y_pin
        self.laser_pin = laser_pin
        self.x_center = x_center
        self.y_center = y_center
        self.x_offset = x_offset
        self.y_offset = y_offset
