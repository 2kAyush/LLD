from enum import Enum

class InkType(str, Enum):
    GEL = "GEL"
    NON_GEL = "NON_GEL"
    FLUID = "FLUID"
    FOUNTAIN = "FOUNTAIN"