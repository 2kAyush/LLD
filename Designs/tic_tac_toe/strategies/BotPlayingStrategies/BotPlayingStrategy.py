from abc import ABC, abstractmethod
from models import Move, Board, Player

class BotPlayingStrategy(ABC):

    @abstractmethod
    def make_next_move(self, board: Board, player: Player) -> Move:
        raise NotImplementedError