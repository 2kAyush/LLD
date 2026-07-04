from typing import Dict
from models import Show

class ShowRepository:
    def __init__(self):
        self.__id = 1
        self.__shows: Dict[int: Show] = {}

    def save(self, show: Show) -> Show:
        show.set_id(self.__id)
        self.__shows[self.__id] = show
        self.__id += 1
        return show

    def get_show(self, show_id) -> Show:
        return self.__shows[show_id]