from typing import Dict
from models import Theatre

class TheatreRepository:
    def __init__(self):
        self.__id = 1
        self.__theatres: Dict[int: Theatre] = {}

    def save(self, theatre: Theatre) -> Theatre:
        theatre.set_id(self.__id)
        self.__theatres[self.__id] = theatre
        self.__id += 1
        return theatre

    def get_theatre(self, theatre_id) -> Theatre:
        return self.__theatres[theatre_id]

    def update(self, theatre_id: int, theatre: Theatre):
        self.__theatres[theatre_id] = theatre