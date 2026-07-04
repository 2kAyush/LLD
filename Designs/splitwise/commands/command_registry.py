from typing import List
from .command import Command

class CommandRegistry:
    def __init__(self):
        # since we will anyways need to initialize all the command
        # classes as they are meant for this application only
        # so we can add them in the registry's constructor only
        self.__command_list: List[Command] = []

    def register(self, command: Command):
        if command in self.__command_list:
            return False
        self.__command_list.append(command)

    def un_register(self, command: Command):
        try:
            self.__command_list.remove(command)
        except ValueError as ve:
            print("command not present in the registry!.")

    def execute(self, input_: str):
        for command in self.__command_list:
            if command.can_execute(input_):
                command.execute(input_)