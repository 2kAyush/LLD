from Enums import SpotType
from models import ParkingSpot, ParkingLot, EntryGate
from .SpotAssignmentStrategy import SpotAssignmentStrategy


class RandomSpotAssignmentStrategy(SpotAssignmentStrategy):
    def assign_spot(self, spotType: SpotType, parking_lot: ParkingLot, entry_gate: EntryGate) -> ParkingSpot:
        for floor in parking_lot.get_parking_floors():
            for spot in floor.get_parking_spots():
                if spot.get_type() == spotType and spot.is_free():
                    return spot

        return None