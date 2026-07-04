from typing import List

from .Base import Base
from .ParkingFloor import ParkingFloor
from .EntryGate import EntryGate
from .ExitGate import ExitGate

class ParkingLot(Base):
    def __init__(self):
        self.__parking_floors = []
        self.__entry_gates = []
        self.__exit_gates = []
        self.__address = ""


    def set_address(self, address: str):
        self.__address = address

    def set_parking_floors(self, parking_floors: List[ParkingFloor]):
        self.__parking_floors = parking_floors

    def set_entry_gates(self, entry_gates: List[EntryGate]):
        self.__entry_gates = entry_gates

    def set_exit_gates(self, exit_gates: List[ExitGate]):
        self.__exit_gates = exit_gates

    def add_parking_floor(self, parking_floor: ParkingFloor):
        self.__parking_floors.append(parking_floor)

    def add_entry_gate(self, entry_gate: EntryGate):
        self.__entry_gates.append(entry_gate)

    def add_exit_gate(self, exit_gate: ExitGate):
        self.__exit_gates.append(exit_gate)

    def get_parking_floors(self):
        return self.__parking_floors

    def get_parking_floor_by_num(self, floor_number: int):
        # id is 1 based
        return self.__parking_floors[floor_number - 1]

    def get_entry_gates(self):
        return self.__entry_gates

    def get_exit_gates(self):
        return self.__exit_gates

    def get_address(self):
        return self.__address