from .BotPlayingStrategy import BotPlayingStrategy
from models import Move, Board, Player

class MediumBotPlayingStrategy(BotPlayingStrategy):

    def make_next_move(self, board: Board, player: Player) -> Move:
        raise NotImplementedError