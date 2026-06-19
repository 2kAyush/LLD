from .BotPlayingStrategy import BotPlayingStrategy
from models import Move, Board, Player

class HardBotPlayingStrategy(BotPlayingStrategy):

    def make_next_move(self, board: Board, player: Player) -> Move:
        raise NotImplementedError