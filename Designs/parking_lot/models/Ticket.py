
from .Base import Base
from .Vehicle import Vehicle
from .ParkingSpot import ParkingSpot
from .EntryGate import EntryGate
from .ParkingLot import ParkingLot
from datetime import datetime

class Ticket(Base):
    def __init__(self):
        self.__entry_time = datetime.now()

    def set_vehicle(self, vehicle: Vehicle):
        self.__vehicle = vehicle

    def set_parking_spot(self, parking_spot: ParkingSpot):
        self.__parking_spot = parking_spot

    def set_gate(self, entry_gate: EntryGate):
        self.__entry_gate = entry_gate

    def set_parking_lot(self, parking_lot: ParkingLot):
        self.__parking_lot = parking_lot

    def get_vehicle(self):
        return self.__vehicle

    def get_parking_spot(self):
        return self.__parking_spot

    def get_entry_gate(self):
        return self.__entry_gate

    def get_entry_time(self):
        return self.__entry_time

    def get_parking_lot(self):
        return self.__parking_lot