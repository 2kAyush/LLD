from Enums import SpotType
from models import ParkingLot, ParkingSpot
from repositories import ParkingLotRepository

class ParkingLotService:
    def __init__(self, parking_lot_repository: ParkingLotRepository):
        self.__parking_lot_repository: ParkingLotRepository = parking_lot_repository

    def create_parking_lot(self, parking_lot: ParkingLot) -> ParkingLot:
        return self.__parking_lot_repository.save(parking_lot)

    def update_address(self, parking_lot_id: int, address: str) -> ParkingLot:
        parking_lot = self.__parking_lot_repository.get_parking_lot(parking_lot_id)
        if parking_lot is None:
            print(f"Parking lot with id {parking_lot_id} not found")
            return parking_lot
        parking_lot.set_address(address)
        return self.__parking_lot_repository.update(parking_lot_id, parking_lot)

    def add_parking_spot(self, parking_lot_id: int, floor_no: int, spot_type: SpotType) -> ParkingLot:
        parking_spot = ParkingSpot(floor_no, spot_type)
        parking_lot = self.__parking_lot_repository.get_parking_lot(parking_lot_id)
        parking_floor = parking_lot.get_parking_floor_by_num(floor_no)
        parking_floor.add_parking_spot(parking_spot)
        return self.__parking_lot_repository.update(parking_lot_id, parking_lot)