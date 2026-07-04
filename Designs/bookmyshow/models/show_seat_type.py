from .base import Base
from enums import SeatType
"""
Every show will have different pricing for every type of seat!.
"""
class ShowSeatType(Base):
    def set_price(self, price: float):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_show(self, show):
        self.__show = show

    def get_show(self):
        return self.__show

    def set_seat_type(self, seat_type: SeatType):
        self.__seat_type = seat_type

    def get_seat_type(self):
        return self.__seat_type