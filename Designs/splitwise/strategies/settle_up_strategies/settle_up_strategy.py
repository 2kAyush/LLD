from typing import List
from abc import ABC, abstractmethod
from models import ExpenseOwingUser, ExpensePayingUser, Transaction

class SettleUpStrategy(ABC):

    @abstractmethod
    def get_transactions(self, paying_expenses: List[ExpensePayingUser], owning_expenses: List[ExpenseOwingUser]) -> List[Transaction]:
        raise NotImplementedError