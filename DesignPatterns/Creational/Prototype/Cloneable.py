from abc import ABC, abstractmethod

class Cloneable(ABC):

    @classmethod
    @abstractmethod
    def Clone(self):
        raise NotImplementedError("Implement this in the function")