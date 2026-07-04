from enums import PaymentMethod, PaymentStatus
from .base import Base
from .ticket import Ticket

class Payment(Base):
    pass

    def set_payment_method(self, payment_method: PaymentMethod):
        self.__payment_method = payment_method

    def get_payment_method(self):
        return self.__payment_method

    def set_time_of_payment(self, time_of_payment):
        self.__time_of_payment = time_of_payment

    def get_time_of_payment(self):
        return self.__time_of_payment

    def set_amount(self, amount: float):
        self.__amount = amount

    def get_amount(self):
        return self.__amount

    def set_reference_id(self, reference_id: str):
        self.__reference_id = reference_id

    def get_reference_id(self):
        return self.__reference_id

    def set_payment_status(self, payment_status: PaymentStatus):
        self.__payment_status = payment_status

    def get_payment_status(self):
        return self.__payment_status

    def set_ticket(self, ticket: Ticket):
        self.__ticket = ticket

    def get_ticket(self):
        return self.__ticket