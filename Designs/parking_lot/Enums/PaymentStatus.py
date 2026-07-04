from enum import Enum

class PaymentStatus(str, Enum):
    SUCCESS = "SUCCESS"
    FAILure = "FAILURE"
    PENDING = "PENDING"