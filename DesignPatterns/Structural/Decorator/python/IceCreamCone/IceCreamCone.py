from abc import ABC, abstractmethod

# interface
class IceCreamCone(ABC):

    @abstractmethod
    def getCost(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def getConstituents(self) -> str:
        raise NotImplementedError