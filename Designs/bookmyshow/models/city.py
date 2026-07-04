from typing import List
from .base import Base
from .theatre import Theatre

class City(Base):
    def __init__(self):
        self.__theatres: List[Theatre] = []

    def set_name(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name

    def add_theatre(self, theatre: Theatre):
        self.__theatres.append(theatre)

    def get_theatres(self):
        return self.__theatres