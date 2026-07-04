from typing import Dict
from models import Movie

class MovieRepository:
    def __init__(self):
        self.__id = 1
        self.__moveis: Dict[int: Movie] = {}

    def save(self, movie: Movie) -> Movie:
        movie.set_id(self.__id)
        self.__moveis[self.__id] = movie
        self.__id += 1
        return movie

    def update(self, movie_id: int, movie: Movie):
        self.__moveis[movie_id] = movie

    def get_movie(self, movie_id) -> Movie:
        return self.__moveis[movie_id]
