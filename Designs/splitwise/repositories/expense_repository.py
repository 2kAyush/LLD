from typing import Dict
from models import Expense

class ExpenseRepository:
    def __init__(self):
        self.__id = 1
        self.__expenses: Dict[int: Expense] = {}

    def save(self, expense: Expense) -> Expense:
        expense.set_id(self.__id)
        self.__expenses[self.__id] = expense
        self.__id += 1
        return expense

    def update(self, expense_id: int, expense: Expense):
        self.__expenses[expense_id] = expense

    def get_expense(self, expense_id) -> Expense:
        return self.__expenses[expense_id]
