from models import ParkingLot
from .ResponseDto import ResponseDto

class UpdateParkingLotResponseDto(ResponseDto):
    def __init__(self):
        self.__parking_lot = None

    def get_parking_lot(self) -> ParkingLot:
        return self.__parking_lot

    def set_parking_lot(self, parking_lot: ParkingLot):
        self.__parking_lot = parking_lot