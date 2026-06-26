from abc import ABC, abstractmethod

class UnlockDiceStrategy(ABC):

    @abstractmethod
    def can_unlock(self, value: int) -> bool:
        raise NotImplementedError