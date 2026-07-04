from enum import Enum

class PaymentMode(str, Enum):
    CASH = "CASH"
    CREDIT_CARD = "CREDIT_CARD"
    DEBIT_CARD = "DEBIT_CARD"
    NETBANKING = "NETBANKING"