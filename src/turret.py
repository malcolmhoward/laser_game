class Turret:
    def __init__(self, x_pin: int, y_pin: int, laser_pin: int,
                 x_center: int, y_center: int,
                 x_cal: int =0, y_cal: int =0):
        """

        :param x_pin:
        :param y_pin:
        :param laser_pin:
        :param x_center:
        :param y_center:
        :param x_cal: Value needed to center the turret
        :param y_cal: Value needed to center the turret
        """
        self.x_pin = x_pin
        self.y_pin = y_pin
        self.laser_pin = laser_pin
        self.x_center = x_center
        self.y_center = y_center
        self.x_cal = x_cal
        self.y_cal = y_cal
