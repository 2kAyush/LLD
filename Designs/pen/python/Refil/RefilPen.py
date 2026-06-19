# Interface name could have been Refillable if we only exposed a method which changes the refil
# but there are multiple methods so not doing that.
# Interface segregation says that there should be as less methods as possible in an interface.
# so this interface is fine as it's only having methods related to refilling properties.

from abc import ABC, abstractmethod
from .Refil import Refil

class RefilPen(ABC):

    @abstractmethod
    def getRefil(self) -> Refil:
        raise NotImplementedError

    @abstractmethod
    def canChangeRefil(self)-> bool:
        raise NotImplementedError

    @abstractmethod
    def changeRefil(self, refil: Refil):
        raise NotImplementedError