from .Player import Player
from Enums import PlayerType
from .Symbol import Symbol
from .Board import Board
from .Move import Move

class HumanPlayer(Player):
    def __init__(self, name, player_type: PlayerType, symbol: Symbol):
        super().__init__(name, player_type, symbol)

    def make_move(self, board: Board):
        row, col = map(
            int,
            input("Enter ',' seperated cell row and col for making move!. (0,0 based)").split(",")
        )
        cell = board.get_cell(row, col)
        if not cell.is_empty():
            # we shall loop over!..
            pass

        return Move(cell, self)