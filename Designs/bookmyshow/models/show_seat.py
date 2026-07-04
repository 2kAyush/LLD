from enums import ShowSeatState

from .base import Base
from .seat import Seat

class ShowSeat(Base):
    def set_show(self, show):
        self.__show = show

    def get_show(self):
        return self.__show

    def set_seat(self, seat: Seat):
        self.__seat = seat

    def get_seat(self):
        return self.__seat

    def set_state(self, state: ShowSeatState):
        self.__state = state

    def get_state(self):
        return self.__state

    def is_available(self) -> bool:
        return self.__state == ShowSeatState.AVAILABLE