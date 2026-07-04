from typing import Dict
from models import User

class UserRepository:
    def __init__(self):
        self.__id = 1
        self.__users: Dict[int: User] = {}

    def save(self, user: User) -> User:
        user.set_id(self.__id)
        self.__users[self.__id] = user
        self.__id += 1
        return user

    def update(self, user_id: int, user: User):
        self.__users[user_id] = user

    def get_user(self, user_id) -> User:
        return self.__users[user_id]
