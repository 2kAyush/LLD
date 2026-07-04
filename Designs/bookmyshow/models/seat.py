from enums import SeatType
from .base import Base

class Seat(Base):
    def set_seat_no(self, seat_num: int):
        self.__seat_no = seat_num

    def set_seat_type(self, seat_type: SeatType):
        self.__seat_type = seat_type

    def get_seat_no(self):
        return self.__seat_no

    def get_seat_type(self):
        return self.__seat_type