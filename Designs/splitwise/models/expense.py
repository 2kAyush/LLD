from typing import List
from .base import Base
from .user import User
from enums import Currency

class Expense(Base):
    def __init__(self):
        self.__description: str = ""
        self.__currency: Currency = ""
        self.__created_by: User = ""
        self.__participants: List[User] = ""
        self.__created_at: str = ""
        self.__amount: int = 0

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value: str):
        self.__description = value

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, value: Currency):
        self.__currency = value

    @property
    def created_by(self):
        return self.__created_by

    @created_by.setter
    def created_by(self, value: User):
        self.__created_by = value

    @property
    def participants(self):
        return self.__participants

    @participants.setter
    def participants(self, value):
        self.__participants = value

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, value):
        self.__created_at = value
