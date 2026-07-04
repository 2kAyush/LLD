from .base import Base

class User(Base):
    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email