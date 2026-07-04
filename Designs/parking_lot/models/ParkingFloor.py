from typing import List
from .Base import Base
from .ParkingSpot import ParkingSpot

class ParkingFloor(Base):
    def __init__(self, floor_number: int):
        self.__parking_spots = []
        self.__floor_number = floor_number

    def get_parking_spots(self):
        return self.__parking_spots

    def get_floor_number(self):
        return self.__floor_number

    def set_parking_spots(self, parking_spots: List[ParkingSpot]):
        self.__parking_spots = parking_spots

    def add_parking_spot(self, parking_spot: ParkingSpot):
        self.__parking_spots.append(parking_spot)
