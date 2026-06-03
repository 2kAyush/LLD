from abc import ABC, abstractmethod

class PathCalculationStrategy(ABC):

    @abstractmethod
    def calculate_path(self, source, destination) -> str:
        raise NotImplementedError