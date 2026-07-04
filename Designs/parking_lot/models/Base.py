from abc import ABC

class Base(ABC):
    def set_id(self, id: int):
        self.__id = id

    def get_id(self):
        return self.__id