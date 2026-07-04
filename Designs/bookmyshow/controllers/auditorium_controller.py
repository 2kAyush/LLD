from models import Auditorium
from repositories import AuditoriumRepository

class AuditoriumService:
    def __init__(self, auditorium_repository: AuditoriumRepository):
        self.__auditorium_repository = auditorium_repository

    def create_auditorium(self, name) -> Auditorium:
        auditorium = Auditorium()
        auditorium.set_name(name)
        return self.__auditorium_repository.save(auditorium)
