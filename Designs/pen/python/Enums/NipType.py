from enum import Enum

class NipType(str, Enum):
    BALL = "BALL"
    NORMAL = "NORMAL"
    FOUNTAIN = "FOUNTAIN"
    SPONGE = "SPONGE"