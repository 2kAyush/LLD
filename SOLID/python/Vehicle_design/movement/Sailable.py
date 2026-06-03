from abc import ABC, abstractmethod

class Sailable(ABC):
    def __init__(self):
        pass

    @classmethod
    @abstractmethod
    def sail(self):
        raise NotImplementedError()