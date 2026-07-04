class CreateUserRequestDto:
    def __init__(self):
        self.__email = ""

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value: str):
        self.__email = value
