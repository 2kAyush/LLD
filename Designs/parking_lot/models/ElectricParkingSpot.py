from .Base import Base
from .ElectricCharger import ElectricCharger
from .ParkingSpot import ParkingSpot

class ElectricParkingSpot(ParkingSpot):
    def __init__(self):
        self.__charger = ElectricCharger()