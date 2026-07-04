from models import ParkingLot
from .ResponseDto import ResponseDto

class CreateParkingLotResponseDto(ResponseDto):
    def __init__(self):
        pass

    def get_parking_lot(self) -> ParkingLot:
        return self.__parking_lot

    def set_parking_lot(self, parking_lot: ParkingLot):
        self.__parking_lot = parking_lot