from Enums import VehicleType

from .Base import Base

class Vehicle(Base):
    def __init__(self, type_: VehicleType, reg_no: str):
        self.__type = type_
        self.__reg_no = reg_no

    def get_type(self):
        return self.__type

    def get_reg_no(self):
        return self.__reg_no