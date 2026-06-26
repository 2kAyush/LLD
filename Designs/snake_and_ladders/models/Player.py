from typing import Dict, List
from .Button import Button
from Enums import ButtonStatus

class Player:
    def __init__(self, id_: int, name: str, colour: str):
        self.__id = id_
        self.__name = name
        self.__buttons: List[Button] = []
        self.__colour = colour
        self.__button_map: Dict[int:Button] = {}

    def set_buttons(self, buttons: List[Button]):
        # because players can be common across multiple games but they
        # will get seperate buttons for each game
        self.__buttons = buttons
        for button in buttons:
            self.__button_map[button.get_id()] = button

    def get_name(self):
        return self.__name

    def get_button_map(self) -> Dict[int,Button]:
        return self.__button_map

    def get_id(self):
        return self.__id

    def get_button(self, id_: int):
        for button in self.__buttons:
            if button.get_id() == id_:
                return button

    def get_colour(self):
        return self.__colour

    def get_buttons(self):
        return self.__buttons

    def get_playable_buttons(self) -> int:
        ans = 0
        for button in self.__buttons:
            if button.get_status() != ButtonStatus.COMPLETED:
                ans += 1
        return ans