from abc import ABC, abstractmethod

class Flyable(ABC):
    def __init__(self):
        pass

    @classmethod
    @abstractmethod
    def fly(self):
        raise NotImplementedError()