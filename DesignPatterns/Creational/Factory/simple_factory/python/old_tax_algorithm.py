from salary_details import SalaryDetails
from tax_algorithm import TaxAlgorithm

class OldTaxAlgorithm(TaxAlgorithm):
    def __init__(self):
        super().__init__()

    def calculateTax(self, salary_details: SalaryDetails) -> float:
        tax = 2.4 * salary_details.base + 3.3 * salary_details.hra
        return tax