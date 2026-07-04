from models import User
from repositories import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    def create_user(self, name, hashed_password, phone_number) -> User:
        user = User()
        user.user_name = name
        user.hashed_password = hashed_password
        user.phone_number = phone_number
        return self.__user_repository.save(user)