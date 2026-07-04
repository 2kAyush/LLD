from commands import CommandRegistry, RegisterUserCommand
from controllers import UserController

while True:
    # takes input from the cli and executes them!..
    # for now only implemented user but others can also be implemented!..
    command_registry = CommandRegistry()
    user_controller = UserController()
    # similarly add settle  up controller, expense controller
    register_user_command = RegisterUserCommand(user_controller)
    command_registry.register(register_user_command)
    # similarly register settle  up command, expense command
    command = input()
    command_registry.execute(command)
