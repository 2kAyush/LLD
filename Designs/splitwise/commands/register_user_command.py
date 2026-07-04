from .command import Command
from enums import Commands
from controllers import UserController

class RegisterUserCommand(Command):
    def __init__(self, user_controller: UserController):
        self.__user_controller = user_controller

    def can_execute(self, command: str) -> bool:
        # Register <name> <Phone> <password>
        command = command.split()
        if len(command) != 4:
            return False
        if command[0] != Commands.REGISTER_USER.value:
            return False

        return True

    def execute(self, command):
        self.__user_controller.register_user(command[1], command[2], command[3])