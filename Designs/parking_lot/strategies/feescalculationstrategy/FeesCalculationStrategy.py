from abc import ABC, abstractmethod
from models import Invoice

class FeesCalculationStrategy(ABC):
    @abstractmethod
    def calculate_fees(self, invoice: Invoice) -> float:
        raise NotImplementedError