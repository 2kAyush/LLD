from typing import List
from enums import ShowFeature, Language

from .base import Base
from .auditorium import Auditorium
from .movie import Movie
from .show_seat import ShowSeat
from .show_seat_type import ShowSeatType

class Show(Base):
    def set_auditorium(self, auditorium: Auditorium):
        self.__auditorium = auditorium

    def get_auditorium(self):
        return self.__auditorium

    def set_movie(self, movie: Movie):
        self.__movie = movie

    def get_movie(self):
        return self.__movie

    def set_start_time(self, start_time):
        self.__start_time = start_time

    def get_start_time(self):
        return self.__start_time

    def set_end_time(self, end_time):
        self.__end_time = end_time

    def get_end_time(self):
        return self.__end_time

    def set_show_seats(self, show_seats: List[ShowSeat]):
        self.__show_seats = show_seats

    def get_show_seats(self):
        return self.__show_seats

    def set_show_seat_type(self, show_seat_type: ShowSeatType):
        self.__show_seat_type = show_seat_type

    def get_show_seat_type(self):
        return self.__show_seat_type

    def set_language(self, language: Language):
        self.__language = language

    def get_language(self):
        return self.__language

    def set_show_features(self, show_features: List[ShowFeature]):
        self.__show_features = show_features

    def get_show_features(self):
        return self.__show_features