from enum import Enum

class VehicleType(str, Enum):
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"
    ELECTRIC = "ELECTRIC"