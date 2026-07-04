from models import User
from repositories import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    def create_user(self, email) -> User:
        user = User()
        user.set_email(email)
        return self.__user_repository.save(user)