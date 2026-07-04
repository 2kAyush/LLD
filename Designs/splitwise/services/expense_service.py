from models import Expense
from repositories import ExpenseRepository

class ExpenseService:
    def __init__(self, expense_repository: ExpenseRepository):
        self.__expense_repository = expense_repository

    def create_expense(self, currency, description, created_by, participants) -> Expense:
        expense = Expense()
        expense.currency = currency
        expense.description = description
        expense.created_by = created_by
        expense.participants = participants
        return self.__expense_repository.save(expense)