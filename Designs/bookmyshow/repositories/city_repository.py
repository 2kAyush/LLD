from typing import Dict
from models import City

class CityRepository:
    def __init__(self):
        self.__id = 1
        self.__cities: Dict[int: City] = {}

    def save(self, city: City) -> City:
        city.set_id(self.__id)
        self.__cities[self.__id] = city
        self.__id += 1
        return city

    def update(self, city_id: int, city: City):
        self.__cities[city_id] = city

    def get_city(self, city_id) -> City:
        return self.__cities[city_id]
