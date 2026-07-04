from models import User

class CreateUserResponseDto:

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user: User):
        self.__user = user
