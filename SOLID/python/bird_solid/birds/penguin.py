from .bird import Bird

class Penguin(Bird):
    def __init__(self, name: str, weight: int, height: int):
        super().__init__(name, weight, height, "penguin")

    def make_sound(self):
        print(f"{self.name} is making peng")

    def eat(self):
        print(f"{self.name} of type {self._type} is eating")