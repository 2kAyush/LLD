from abc import ABC, abstractmethod

class Drivable(ABC):
    def __init__(self):
        pass

    @classmethod
    @abstractmethod
    def drive(self):
        raise NotImplementedError()