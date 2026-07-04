from .Base import Base
from Enums import PaymentMode, PaymentStatus

class Payment(Base):
    def __init__(self, id_: int, payment_mode: PaymentMode, bill: int, payment_status: PaymentStatus):
        self.set_id(id_)
        self.__bill = bill
        self.__payment_mode = payment_mode
        self.__payment_status = payment_status

    def get_invoice(self):
        return self.__invoice

    def get_payment_mode(self):
        return self.__payment_mode

    def get_payment_status(self):
        return self.__payment_status