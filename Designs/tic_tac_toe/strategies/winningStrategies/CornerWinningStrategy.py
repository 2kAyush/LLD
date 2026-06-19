from models import Move, Board
from .WinningStrategy import WinningStrategy

class CornerWinningStrategy(WinningStrategy):

    def check_win(self, move: Move, board: Board) -> bool:
        # check for cornerns only!.
        won = True
        symbol = move.get_symbol()
        dimension = board.get_dimension()
        # check if the move made was in any of the corners.
        row = move.get_cell().get_row()
        col = move.get_cell().get_col()
        board = board.get_board()
        return False