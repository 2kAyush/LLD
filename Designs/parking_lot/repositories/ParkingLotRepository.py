from typing import Dict
from models import ParkingLot

class ParkingLotRepository:
    def __init__(self):
        self.__id_counter = 0
        self.__parking_lots: Dict[int, ParkingLot] = {}

    def save(self, parking_lot: ParkingLot) -> ParkingLot:
        self.__id_counter += 1
        parking_lot.set_id(self.__id_counter)
        self.__parking_lots[self.__id_counter] = parking_lot
        return parking_lot

    def update(self, id: int, parking_lot: ParkingLot) -> ParkingLot:
        self.__parking_lots[id] = parking_lot
        return parking_lot

    def get_parking_lot(self, id: int) -> ParkingLot:
        return self.__parking_lots.get(id)

    def get_all_parking_lots(self) -> Dict[int, ParkingLot]:
        return self.__parking_lots