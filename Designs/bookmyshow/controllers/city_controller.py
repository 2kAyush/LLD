from models import City
from services import CityService

class CityController:
    def __init__(self, city_service: CityService):
        self.__city_service = city_service

    def create_city(self, name) -> City:
        return self.__city_service.create_city(name)

    def add_theatre(self, city_id, theatre):
        self.__city_service.add_theatre(city_id, theatre)
