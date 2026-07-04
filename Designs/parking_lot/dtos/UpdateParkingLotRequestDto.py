class UpdateParkingLotRequestDto:
    def __init__(self):
        self.__parking_lot_id = None
        self.__address = None

    def get_parking_lot_id(self) -> str:
        return self.__parking_lot_id

    def get_address(self) -> str:
        return self.__address

    def set_parking_lot_id(self, parking_lot_id: str):
        self.__parking_lot_id = parking_lot_id

    def set_address(self, address: str):
        self.__address = address