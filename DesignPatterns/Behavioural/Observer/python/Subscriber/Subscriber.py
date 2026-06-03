from abc import ABC, abstractmethod

# This subscriber interface can be generic
class Subscriber(ABC):

    @abstractmethod
    def listen(self, order): # order can be dynamic
        raise NotImplementedError
