from enum import Enum

class PaymentStatus(str, Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"