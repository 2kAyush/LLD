from typing import List
from .base import Base
from .user import User
from .show import Show
from .show_seat import ShowSeat

from enums import TicketStatus

class Ticket(Base):

    def __init__(self):
        self.__booked_by = None

    def set_booked_by(self, booked_by: User):
        self.__booked_by = booked_by

    def get_booked_by(self):
        return self.__booked_by

    def set_show(self, show: Show):
        self.__show = show

    def get_show(self):
        return self.__show

    def set_show_seats(self, show_seats: List[ShowSeat]):
        self.__show_seats = show_seats

    def get_show_seats(self):
        return self.__show_seats

    def set_total_amount(self, total_amount: float):
        self.__total_amount = total_amount

    def get_total_amount(self):
        return self.__total_amount

    def set_ticket_status(self, ticket_status: TicketStatus):
        self.__ticket_status = ticket_status

    def get_ticket_status(self):
        return self.__ticket_status

    def set_time_of_booking(self, time_of_booking):
        self.__time_of_booking = time_of_booking

    def get_time_of_booking(self):
        return self.__time_of_booking
