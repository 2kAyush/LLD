from abc import ABC, abstractmethod

class WinningStrategy(ABC):

    @abstractmethod
    def check_win(self, move, board) -> bool:
        raise NotImplementedError