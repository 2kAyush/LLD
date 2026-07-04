from models import Theatre
from repositories import TheatreRepository, CityRepository

class TheatreService:
    def __init__(self, theatre_repository: TheatreRepository, city_repository: CityRepository):
        self.__theatre_repository = theatre_repository
        self.__city_repository = city_repository

    def create_theatre(self, name, city_id: int) -> Theatre:
        city = self.__city_repository.get_city(city_id)
        if not city:
            print("invalid city id provided")
            return None
        theatre = Theatre()
        theatre.set_name(name)
        theatre = self.__theatre_repository.save(theatre)


        city.add_theatre(theatre)
        self.__city_repository.update(city_id, city)
