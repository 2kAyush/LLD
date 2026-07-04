from Enums import SpotType, ParkingSpotStatus
from .Base import Base

class ParkingSpot(Base):
    def __init__(self, floor_no: int, type_: SpotType):
        self.__floor_no = floor_no
        self.__type = type_
        self.__status = ParkingSpotStatus.AVAILABLE

    def get_floor_no(self):
        return self.__floor_no

    def get_type(self):
        return self.__type

    def get_spot_status(self):
        return self.__status

    def is_free(self) -> bool:
        return self.__status == ParkingSpotStatus.AVAILABLE
