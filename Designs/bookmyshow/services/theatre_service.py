from models import Theatre
from repositories import TheatreRepository

class TheatreService:
    def __init__(self, theatre_repository: TheatreRepository):
        self.__theatre_repository = theatre_repository

    def create_threatre(self, name) -> Theatre:
        theatre = Theatre()
        theatre.set_name(name)
        return self.__theatre_repository.save(theatre)

    def add_auditorium(self, theatre_id, auditorium):
        theatre = self.__theatre_repository.get_theatre(theatre_id)
        theatre.add_auditorium(auditorium)
        self.__theatre_repository.update(theatre_id, theatre)
