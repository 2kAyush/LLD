from abc import ABC, abstractmethod
from models import ParkingSpot, ParkingLot, EntryGate
from Enums import SpotType

class SpotAssignmentStrategy(ABC):
    @abstractmethod
    def assign_spot(self, spotType: SpotType, parking_lot: ParkingLot, entry_gate: EntryGate) -> ParkingSpot:
        raise NotImplementedError