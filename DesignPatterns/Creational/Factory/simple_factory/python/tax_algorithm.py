from abc import ABC, abstractmethod
from salary_details import SalaryDetails

class TaxAlgorithm(ABC):

    @classmethod
    @abstractmethod
    def calculateTax(self, salary_details: SalaryDetails) -> float:
        raise NotImplementedError("not Implemented")