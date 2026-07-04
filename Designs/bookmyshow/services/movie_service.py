from models import Movie
from repositories import MovieRepository

class MovieService:
    def __init__(self, movie_repository: MovieRepository):
        self.__movie_repository = movie_repository

    def create_movie(self, name, actors, length, movie_features, rating) -> Movie:
        movie = Movie()
        movie.set_name(name)
        movie.set_actors(actors)
        movie.set_length(length)
        movie.set_movie_features(movie_features)
        movie.set_rating(rating)
        return self.__movie_repository.save(movie)