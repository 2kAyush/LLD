from tax_algorithm import TaxAlgorithm
from old_tax_algorithm import OldTaxAlgorithm
from new_tax_algorithm import NewTaxAlgorithm
from tax_regime import TaxRegime

class TaxCalculatorFactory:

    @staticmethod
    def getTaxAlgorithm(regime: TaxRegime) -> TaxAlgorithm:
        if regime == TaxRegime.OLD:
            return OldTaxAlgorithm()
        elif regime == TaxRegime.NEW:
            return NewTaxAlgorithm()