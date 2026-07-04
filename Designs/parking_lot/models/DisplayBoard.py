from typing import Dict

from .Base import Base
from Enums import SpotType

class DisplayBoard(Base):
    def __init__(self):
        super().__init__()
        self.__map: Dict[SpotType, int] = {}

    def update_spot_availablilty(self, spot_type: SpotType, ctr):
        if spot_type not in self.__map:
            self.__map[spot_type] = 0
        self.__map[spot_type] += ctr

    def get_availability(self, spot_type: SpotType):
        # maybe not required here!..
        return self.__map[spot_type]