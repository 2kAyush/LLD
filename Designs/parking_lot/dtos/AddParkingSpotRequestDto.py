from Enums import SpotType

class AddParkingSpotRequestDto:
    def set_parking_lot_id(self, id_: int):
        self.__parking_lot_id = id_

    def set_floor_no(self, num: int):
        self.__floor_no = num

    def set_spot_type(self, spot_type: SpotType):
        self.__spot_type = spot_type

    def get_parking_lot_id(self):
        return self.__parking_lot_id

    def get_floor_no(self):
        return self.__floor_no

    def get_spot_type(self):
        return self.__spot_type