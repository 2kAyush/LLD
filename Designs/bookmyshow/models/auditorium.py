from typing import List

from enums import AuditoriumFeature
from .seat import Seat
from .base import Base

class Auditorium(Base):
    def set_audi_features(self, audi_features: List[AuditoriumFeature]):
        self.__audi_features = audi_features

    def set_name(self, name):
        self.__name = name

    def set_capacity(self, capacity):
        self.__capacity = capacity

    def set_theater(self, theatre):
        self.__theatre = theatre

    def set_seats(self, seats: List[Seat]):
        self.__seats = seats

    def get_seats(self):
        return self.__seats

    def get_theater(self):
        return self.__theatre

    def get_capacity(self):
        return self.__capacity

    def get_name(self):
        return self.__name

    def get_audi_features(self):
        return self.__audi_features