from .bird import Bird
from interfaces.flyable import FlyableInterface
from interfaces.flying_behaviour import FlyingBehaviourInterface

class Crow(Bird, FlyableInterface):
    def __init__(self, name: str, weight: int, height: int, flying_strategy: FlyingBehaviourInterface):
        super().__init__(name, weight, height, "crow")
        self.flying_strategy = flying_strategy

    def make_sound(self):
        print(f"{self.name} is making Caw Caw")

    def eat(self):
        print(f"{self.name} of type {self._type} is eating")

    def fly(self):
        self.flying_strategy.make_fly(self.name, self._type)