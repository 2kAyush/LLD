from abc import ABC, abstractmethod

class FlyingBehaviourInterface(ABC):
    @abstractmethod
    def make_fly(self, name, _type):
        raise NotImplementedError("fly method should be implemented by child classes")
