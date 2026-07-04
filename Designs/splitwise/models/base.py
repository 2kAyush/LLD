from abc import ABC

class Base(ABC):
    def set_id(self, id_: int):
        self.__id = id_

    def get_id(self):
        return self.__id