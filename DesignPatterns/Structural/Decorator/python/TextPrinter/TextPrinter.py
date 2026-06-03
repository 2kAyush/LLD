from abc import ABC, abstractmethod

class TextPrinter(ABC):

    @abstractmethod
    def getText(self) -> str:
        raise NotImplementedError