from models import Vehicle, EntryGate
from Enums import SpotType

class GenerateTicketRequestDto:
    def set_vehicle(self, vehicle: Vehicle):
        self.__vehicle = vehicle

    def set_entry_gate(self, entry_gate: EntryGate):
        self.__entry_gate = entry_gate

    def set_parking_lot_id(self, id: int):
        self.__parking_lot_id = id

    def get_vehicle(self):
        return self.__vehicle

    def set_spot_type(self, spot_type: SpotType):
        self.__spot_type = spot_type

    def get_spot_type(self):
        return self.__spot_type

    def get_entry_gate(self):
        return self.__entry_gate

    def get_parking_lot_id(self):
        return self.__parking_lot_id