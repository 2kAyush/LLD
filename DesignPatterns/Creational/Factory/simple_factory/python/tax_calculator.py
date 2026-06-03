from tax_regime import TaxRegime
from salary_details import SalaryDetails

from tax_calculator_factory import TaxCalculatorFactory

class TaxCalculator:

    @staticmethod
    def calculate_tax(regime : TaxRegime, salarydetails: SalaryDetails):
        return TaxCalculatorFactory.getTaxAlgorithm(regime).calculateTax(salarydetails)


# client:
if __name__ == "__main__":
    salary_details = SalaryDetails(10, 2, 1)
    print("for old: ", TaxCalculator.calculate_tax(TaxRegime.OLD, salary_details))
    print("for old: ", TaxCalculator.calculate_tax(TaxRegime.NEW, salary_details))