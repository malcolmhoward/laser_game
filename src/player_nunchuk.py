"""
Defines the data associated with a player's nunchuk
"""


class PlayerNunchuk:
    def __init__(self, x_center, y_center, x_min, x_max, y_min, y_max):
        self.x_center = x_center
        self.y_center = y_center
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
