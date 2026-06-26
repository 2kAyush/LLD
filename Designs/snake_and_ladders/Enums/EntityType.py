from enum import Enum

class EntityType(str, Enum):
    SNAKE = "SNAKE"
    LADDER = "LADDER"
    FROG = "FROG"
    NEXT_PRIME = "NEXT_PRIME"