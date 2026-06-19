from abc import ABC, abstractmethod
from Enums import Pentype, Colour
from strategies.writeStrategies import *

class Pen(ABC):
    def __init__(self, pentype: Pentype, writeBehaviour: WriteBehaviour):
        self.__pentype = pentype
        self.__writeBehaviour = writeBehaviour

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_company(self):
        return self.__company

    def set_company(self, company):
        self.__company = company

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_pentype(self):
        return self.__pentype

    def set_pentype(self, pentype):
        self.__pentype = pentype

    def write(self):
        self.__writeBehaviour.write()


    @abstractmethod
    def getColour(self) -> Colour:
        raise NotImplementedError