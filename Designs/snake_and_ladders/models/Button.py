from Enums import *

class Button:
    def __init__(self, id_: int):
        self.__position: int = 0
        self.__id = id_
        self.__status: ButtonStatus = ButtonStatus.LOCKED

    def set_button_status(self, status: ButtonStatus):
        self.__status = status

    def set_position(self, position : int):
        self.__position = position

    def get_position(self):
        return self.__position

    def get_status(self):
        return self.__status

    def get_id(self):
        return self.__id