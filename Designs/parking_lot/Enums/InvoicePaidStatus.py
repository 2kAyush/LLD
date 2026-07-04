from enum import Enum

class InvoicePaidStatus(str, Enum):
    PAID = "PAID"
    UNPAID = "UNPAID"