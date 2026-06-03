from enum import Enum

class TaxRegime(str, Enum):
    NEW = "new"
    OLD = "old"