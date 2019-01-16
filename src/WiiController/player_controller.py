from src.player_controller import  PlayerController
from .classic_controller import ClassicController
from .pro_controller import ProController
from .nunchuk import Nunchuk

class PlayerNunchuk(PlayerController):
    def __init__(self, x_center, y_center, x_min, x_max, y_min, y_max):
        super().__init__(x_center, y_center, x_min, x_max, y_min, y_max)
        try:
            self.n = Nunchuk()
        except OSError:
            raise OSError('Ensure the controller is plugged in') from None

    def joystick(self):
        return self.n.joystick()

    def fire(self):
        return self.n.button_z()


class PlayerLeftPro(PlayerController):
    def __init__(self, x_center, y_center, x_min, x_max, y_min, y_max, pro):
        super().__init__(x_center, y_center, x_min, x_max, y_min, y_max)
        if pro is None:
            try:
                self.pro = ProController()
            except OSError:
                raise OSError('Ensure the controller is plugged in') from None
        else:
            self.pro = pro

    def joystick(self):
        return self.pro.left_joystick()

    def fire(self):
        return self.pro.button_zl()


class PlayerRightPro(PlayerController):
    def __init__(self, x_center, y_center, x_min, x_max, y_min, y_max, pro=None):
        super().__init__(x_center, y_center, x_min, x_max, y_min, y_max)
        if pro is None:
            try:
                self.pro = ProController()
            except OSError:
                raise OSError('Ensure the controller is plugged in') from None
        else:
            self.pro = pro

    def joystick(self):
        return self.pro.right_joystick()

    def fire(self):
        return self.pro.button_zr()


class PlayerLeftClassic(PlayerController):
    def __init__(self, x_center, y_center, x_min, x_max, y_min, y_max, classic):
        super().__init__(x_center, y_center, x_min, x_max, y_min, y_max)
        if classic is None:
            try:
                self.classic = ClassicController()
            except OSError:
                raise OSError('Ensure the controller is plugged in') from None
        else:
            self.classic = classic

    def joystick(self):
        return self.classic.left_joystick()

    def fire(self):
        return self.classic.button_zl()


class PlayerRightClassic(PlayerController):
    def __init__(self, x_center, y_center, x_min, x_max, y_min, y_max, classic=None):
        super().__init__(x_center, y_center, x_min, x_max, y_min, y_max)
        if classic is None:
            try:
                self.classic = ClassicController()
            except OSError:
                raise OSError('Ensure the controller is plugged in') from None
        else:
            self.classic = classic

    def joystick(self):
        return self.classic.right_joystick()

    def fire(self):
        return self.classic.button_zr()


def pro_controller_factory():
    try:
        pro = ProController()
    except OSError:
        raise OSError('Ensure the controller is plugged in') from None
    left = PlayerLeftPro(32, 32, 5, 59, 5, 59, pro=pro)
    right = PlayerRightPro(16, 16, 3, 29, 3, 29, pro=pro)
    return left, right


def classic_controller_factory():
    try:
        classic = ClassicController()
    except OSError:
        raise OSError('Ensure the controller is plugged in') from None
    left = PlayerLeftClassic(32, 32, 5, 59, 5, 59, classic=classic)
    right = PlayerRightClassic(16, 16, 3, 29, 3, 29, classic=classic)
    return left, right
