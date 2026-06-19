from Enums import PlayerType, BotDifficultyLevel
from Factory import BotPlayingStrategyFactory
from .Board import Board
from .Player import Player
from .Symbol import Symbol
from .Move import Move

class BotPlayer(Player):
    def __init__(
            self,
            player_type: PlayerType,
            symbol: Symbol,
            bot_difficulty_level: BotDifficultyLevel,
        ):
        self.bot_difficulty_level = bot_difficulty_level
        self.bot_playing_strategy = (
            BotPlayingStrategyFactory().
            createBotPlayingStrategyForDifficutlyLevel(
                bot_difficulty_level
            )
        )
        super().__init__("BOT", player_type, symbol)

    def make_move(self, board: Board) -> Move:
        move = self.bot_playing_strategy.make_next_move(board, self)
        return move
