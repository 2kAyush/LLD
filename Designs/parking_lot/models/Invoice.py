from .Base import Base
from .Ticket import Ticket
from Enums import InvoicePaidStatus, PaymentMode, PaymentStatus
from datetime import datetime

class Invoice(Base):
    def __init__(self, id_: int, ticket: Ticket, operator: str):
        self.set_id(id_)
        self.__ticket = ticket
        self.__amount = 0
        self.__operator = operator
        self.__paid_status = InvoicePaidStatus.UNPAID

        self.__exit_time = None

    # getters and setters
    def get_ticket(self):
        return self.__ticket

    def get_amount(self):
        return self.__amount

    def get_operator(self):
        return self.__operator

    def get_paid_status(self):
        return self.__paid_status

    def get_exit_time(self):
        return self.__exit_time

    def set_amount(self, amount: int):
        self.__amount = amount

    def set_operator(self, operator: str):
        self.__operator = operator

    def set_paid_status(self, paid_status: InvoicePaidStatus):
        self.__paid_status = paid_status

    def set_exit_time(self, exit_time: datetime):
        self.__exit_time = exit_time