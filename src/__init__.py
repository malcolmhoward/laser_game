from .npc import NPC
try:
    import RPi.GPIO as rpi
except (RuntimeError, ImportError) as e:
    # TODO: Add error-specific messaging.
    print("RuntimeError: This module can only be run on a Raspberry Pi!")
    print("Setting rpi to None..")
    rpi = None

from .player import Player
from .player_controller import PlayerController
from .WiiController.player_controller import *
