import time

from models import Show
from repositories import ShowRepository

class ShowService:
    def __init__(self, show_repository: ShowRepository):
        self.__show_repository = show_repository

    def create_show(
            self,
            auditorium,
            language,
            start_time,
            end_time,
            movie,
            show_features,
            show_seats,
            show_seat_types
        ) -> Show:
        show = Show()
        show.set_auditorium(auditorium)
        show.set_start_time(start_time)
        show.set_end_time(end_time)
        show.set_language(language)
        show.set_movie(movie)
        show.set_show_features(show_features)
        show.set_show_seat_type(show_seat_types)
        show.set_show_seats(show_seats)
        return self.__show_repository.save(show)
