from .base import Base

class Actor(Base):
    def __init__(self):
        self.__movies = []

    def set_name(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name

    def add_movie(self, movie):
        self.__movies.append(movie)