from enum import Enum

class ShowSeatState(str, Enum):
    BOOKED = "BOOKED"
    AVAILABLE = "AVAILABLE"
    LOCKED = "LOCKED"
