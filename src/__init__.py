from .npc import NPC
try:
    import RPi.GPIO as rpi
except Exception as e:
    if e.__class__.__name__ == "RuntimeError":
        print("RuntimeError: This module can only be run on a Raspberry Pi!")
        print("Setting rpi to None..")
        rpi = None
    else:
        raise(e)
from .player import Player
from .player_controller import PlayerController
