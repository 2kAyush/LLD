from typing import Dict
from models import Auditorium

class AuditoriumRepository:
    def __init__(self):
        self.__id = 1
        self.__auditoriums: Dict[int: Auditorium] = {}

    def save(self, auditorium: Auditorium) -> Auditorium:
        auditorium.set_id(self.__id)
        self.__auditoriums[self.__id] = auditorium
        self.__id += 1
        return auditorium

    def get_auditorium(self, audi_id) -> Auditorium:
        return self.__auditoriums[audi_id]

    def update(self, audi_id: int, audi: Auditorium):
        self.__auditoriums[audi_id] = audi