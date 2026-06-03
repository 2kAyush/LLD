from abc import ABC, abstractmethod

class EnergySource(ABC):
    def __init__(self):
        pass

    @classmethod
    @abstractmethod
    def refill(self, amount: float):
        print("raising exception as this is an interface")
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def consume(self, amount: float):
        print("raising exception as this is an interface")
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def getRemainingEnergy(self) -> float:
        print("raising exception as this is an interface")
        raise NotImplementedError()