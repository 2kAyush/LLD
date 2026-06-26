from enum import Enum

class GameStatus(str, Enum):
    RUNNING = "RUNNING"
    NOT_STARTED_YET = "NOT_STARTED_YET"
    OVER = "OVER"