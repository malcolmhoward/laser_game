import json
from .turret import Turret

with open('src/calibration.json', 'r') as json_file:
    cal = json.load(json_file)

TURRET_1 = Turret(0, 1, 4, 375, 375, x_cal=cal['turret1']['x'],
                                      y_cal=cal['turret1']['y'])
TURRET_2 = Turret(2, 3, 17, 375, 375, x_cal=cal['turret2']['x'],
                                      y_cal=cal['turret2']['y'])
TURRET_3 = Turret(4, 5, 18, 375, 375, x_cal=cal['turret3']['x'],
                                     y_cal=cal['turret3']['y'])
TURRET_4 = Turret(6, 7, 27, 375, 375, x_cal=cal['turret4']['x'],
                                     y_cal=cal['turret4']['y'])
TURRET_5 = Turret(8, 9, 22, 375, 375, x_cal=cal['turret5']['x'],
                                     y_cal=cal['turret6']['y'])
