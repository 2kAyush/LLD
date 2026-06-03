from abc import ABC, abstractmethod

class FlyableInterface(ABC):
    @abstractmethod
    def fly(self):
        raise NotImplementedError("fly method should be implemented by child classes")
