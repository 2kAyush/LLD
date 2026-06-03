from abc import ABC, abstractmethod

class Pizza(ABC):

    @abstractmethod
    def getCost(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def getConstituents(self) -> str:
        raise NotImplementedError