from abc import ABC, abstractmethod

class Bird(ABC):
    def __init__(self, name: str, weight: int, height: int, _type: str):
        self.name = name
        self.weight = weight
        self.height = height
        self._type = _type

    @abstractmethod
    def eat(self):
        raise NotImplementedError("eat method should be implemented by child classes")

    @abstractmethod
    def make_sound(self):
        raise NotImplementedError("make sound method should be implemented by child classes")
