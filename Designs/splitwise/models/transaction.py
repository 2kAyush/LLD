from .base import Base
from .user import User

class Transaction(Base):
    def __init__(self, user_to_pay: User, paying_user: User, amount: float):
        self.__user_to_pay = user_to_pay
        self.__paying_user = paying_user
        self.__amount = amount

    @property
    def user_to_pay(self):
        return self.__user_to_pay

    @user_to_pay.setter
    def user_to_pay(self, value):
        self.__user_to_pay = value

    @property
    def paying_user(self):
        return self.__paying_user

    @paying_user.setter
    def paying_user(self, value):
        self.__paying_user = value

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value
