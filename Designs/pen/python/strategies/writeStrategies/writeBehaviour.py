from abc import ABC, abstractmethod

class WriteBehaviour(ABC):

    @abstractmethod
    def write(self):
        raise NotImplementedError