from enum import Enum

class SeatType(str, Enum):
    VIP = "VIP"
    PLATINUM = "PLATINUM"
    GOLD = "GOLD"
    SILVER = "SILVER"