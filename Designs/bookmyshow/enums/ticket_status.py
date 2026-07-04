from enum import Enum

class TicketStatus(str, Enum):
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
