from .base import Base
from .expense import Expense
from .user import User

class ExpenseOwingUser(Base):
    def __init__(self):
        self.__user: User = ""
        self.__expense: Expense = ""
        self.__amount: float = 0

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, value):
        self.__user = value

    @property
    def expense(self):
        return self.__expense

    @expense.setter
    def expense(self, value):
        self.__expense = value

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value
