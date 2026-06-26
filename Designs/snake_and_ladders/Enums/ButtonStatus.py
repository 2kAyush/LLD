from enum import Enum

class ButtonStatus(str, Enum):
    LOCKED = "LOCKED"
    IN_GAME = "IN_GAME"
    COMPLETED = "COMPLETED"