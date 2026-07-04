from typing import List

from .auditorium import Auditorium
from .base import Base

class Theatre(Base):
    def set_name(self, name):
        self.__name = name
        self.__auditoriums: List[Auditorium] = []

    def get_address(self, address):
        self.__address = address

    def get_address(self):
        return self.__address

    def get_name(self):
        return self.__name

    def set_auditoriums(self, auditoriums: List[Auditorium]):
        self.__auditoriums = auditoriums

    def get_auditoriums(self):
        return self.__auditoriums

    def set_shows(self, shows):
        self.__shows = shows

    def get_shows(self):
        return self.__shows

    def add_auditorium(self, auditorium: Auditorium):
        self.__auditoriums.append(auditorium)