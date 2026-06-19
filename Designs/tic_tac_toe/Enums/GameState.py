from enum import Enum

class GameState(str, Enum):
    WON = "WON"
    DRAW = "DRAW"
    RUNNING = "RUNNING"
    NOT_STARTED_YET = "NOT_STARTED_YET"