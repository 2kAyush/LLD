from abc import ABC, abstractmethod
from Enums import EntityType
class ForeignEntity(ABC):
    def __init__(self, from_: int, to_: int, type_ : EntityType):
        self.__from = from_
        self.__to = to_
        self.__type = type_

    def get_from(self) -> int:
        return self.__from

    def get_type(self):
        return self.__type

    def get_to(self) -> int:
        return self.__to