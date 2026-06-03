from .bird import Bird

class Ostrich(Bird):
    def __init__(self, name: str, weight: int, height: int):
        super().__init__(name, weight, height, "ostrich")

    def make_sound(self):
        print(f"{self.name} is making runnnnnn")

    def eat(self):
        print(f"{self.name} of type {self._type} is eating")