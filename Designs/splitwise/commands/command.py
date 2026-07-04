from abc import ABC, abstractmethod

class Command(ABC):

    @abstractmethod
    def can_execute(command: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def execute(command: str):
        raise NotImplementedError