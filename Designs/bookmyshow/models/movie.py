from typing import List
from enums import Language, MovieFeature
from .base import Base

class Movie(Base):
    def set_name(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name

    def languages(self, languages: List[Language]):
        self.__languages = languages

    def get_languages(self):
        return self.__languages

    def set_rating(self, rating: float):
        self.__rating = rating

    def get_rating(self):
        return self.__rating

    def set_actors(self, actors):
        self.__actors = actors

    def get_actors(self):
        return self.__actors

    def set_length(self, length: int):
        self.__length = length

    def get_length(self):
        return self.__length

    def set_movie_features(self, movie_features: List[MovieFeature]):
        self.__movie_features = movie_features

    def get_movie_features(self):
        return self.__movie_features
