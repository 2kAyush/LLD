from typing import Dict
from models import ExpenseOwingUser

class ExpenseOwingUserRepository:
    def __init__(self):
        self.__id = 1
        self.__expenses: Dict[int: ExpenseOwingUser] = {}

    def save(self, expense: ExpenseOwingUser) -> ExpenseOwingUser:
        expense.set_id(self.__id)
        self.__expenses[self.__id] = expense
        self.__id += 1
        return expense

    def update(self, expense_id: int, expense: ExpenseOwingUser):
        self.__expenses[expense_id] = expense

    def get_expense(self, expense_id) -> ExpenseOwingUser:
        return self.__expenses[expense_id]
