from Enums import RefilType

from .Ink import Ink
from .Nip import Nip

class Refil:
    def __init__(self, ink: Ink, type_: RefilType, nip: Nip, total_ink: int):
        self.__ink = ink
        self.__type = type_
        self.__nip = nip
        self.__total_ink = total_ink

    def getColour(self):
        return self.__ink.getColour()

    def getLeftInk(self):
        return self.__total_ink

    def get_type(self):
        return self.__type

    def get_nip(self):
        return self.__nip