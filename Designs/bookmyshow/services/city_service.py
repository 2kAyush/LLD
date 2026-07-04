from models import City
from repositories import CityRepository

class CityService:
    def __init__(self, city_repository: CityRepository):
        self.__city_repository = city_repository

    def create_city(self, name) -> City:
        city = City()
        city.set_name(name)
        return self.__city_repository.save(city)

    def add_theatre(self, city_id: int, theatre):
        city = self.__city_repository.get_city(city_id)
        city.add_theatre(theatre)
        self.__city_repository.update(city_id, city)