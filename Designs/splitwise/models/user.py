from .base import Base

class User(Base):
    def __init__(self):
        self.__user_name: str = ""
        self.__phone_number: str = ""
        self.__hashed_password: str = ""

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        self.__phone_number = value

    @property
    def hashed_password(self):
        return self.__hashed_password

    @hashed_password.setter
    def hashed_password(self, value):
        self.__hashed_password = value


    @property
    def user_name(self):
        return self.__user_name

    @user_name.setter
    def user_name(self, user_name):
        self.__user_name = user_name