from .bird import Bird
from interfaces.flyable import FlyableInterface

class Pigeon(Bird, FlyableInterface):
    def __init__(self, name: str, weight: int, height: int):
        super().__init__(name, weight, height, "pigeon")

    def make_sound(self):
        print(f"{self.name} is making chirpppp")

    def eat(self):
        print(f"{self.name} of type {self._type} is eating")

    def fly(self):
        print(f"{self.name} of type {self._type} is flying")