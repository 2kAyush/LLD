from .Base import Base
from Enums import GateStatus, GateType

class Gate(Base):
    def __init__(self, number, operator, gate_type: GateType, gate_status: GateStatus):
        self.__number = number
        self.__operator = operator
        self.__gate_type = gate_type
        self.__status = gate_status

    def get_number(self):
        return self.__number

    def get_operator(self):
        return self.__operator

    def get_gate_type(self):
        return self.__gate_type

    def get_status(self):
        return self.__status