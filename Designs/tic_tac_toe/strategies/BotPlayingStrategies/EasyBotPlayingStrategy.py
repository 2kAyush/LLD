from .BotPlayingStrategy import BotPlayingStrategy
from models import Move, Board, Player

class EasyBotPlayingStrategy(BotPlayingStrategy):

    def make_next_move(self, board: Board, player: Player) -> Move:
        move = None
        for cell_list in board.get_board():
            for cell in cell_list:
                if cell.is_empty():
                    move = Move(cell, player)
        print("Making Bot Move")
        return move
