from models import Auditorium
from repositories import AuditoriumRepository

class AuditoriumService:
    def __init__(self, auditorium_repository: AuditoriumRepository):
        self.__auditorium_repository = auditorium_repository

    def create_auditorium(self, name, theatre, seats, capacity, audi_features) -> Auditorium:
        auditorium = Auditorium()
        auditorium.set_name(name)
        auditorium.set_capacity(capacity)
        auditorium.set_theater(theatre)
        auditorium.set_audi_features(audi_features)
        auditorium.set_seats(seats)
        return self.__auditorium_repository.save(auditorium)
