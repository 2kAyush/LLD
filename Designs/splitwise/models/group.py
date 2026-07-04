import time

from typing import List
from .base import Base
from .user import User

class Group(Base):
    def __init__(self):
        self.__name: str = ""
        self.__participants: List[User] = []
        self.__admins: List[User] = []
        self.created_by: User = None
        self.__create_time: time = ""

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def participants(self):
        return self.__participants

    @participants.setter
    def participants(self, value):
        self.__participants = value

    @property
    def admins(self):
        return self.__admins

    @admins.setter
    def set_admins(self, value):
        self.__admins = value

    @property
    def created_by(self):
        return self.created_by

    @created_by.setter
    def created_by(self, value):
        self.created_by = value

    @property
    def create_time(self):
        return self.__create_time

    @create_time.setter
    def create_time(self, value):
        self.__create_time = value
