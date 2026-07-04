from enum import Enum

class GateStatus(str, Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"