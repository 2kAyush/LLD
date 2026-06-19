from models import Move, Board

from .WinningStrategy import WinningStrategy

class NormalWinningStrategy(WinningStrategy):

    def check_win(self, move: Move, board: Board) -> bool:
        won = True
        symbol = move.get_symbol()
        dimension = board.get_dimension()
        # check for rows, cols
        row = move.get_cell().get_row()
        col = move.get_cell().get_col()
        board = board.get_board()
        for i in range(dimension):
            if (
                board[row][i].get_symbol() != symbol
                or
                board[i][col].get_symbol() != symbol
            ):
                won = False
                break

        # check for diangonals
        # sits in left diagonal
        if row == col:
            for i in range(dimension):
                if board[i][i] != symbol:
                    won = False
                    break

        # right diagonal
        r_r = 0
        r_c = dimension - 1
        while r_r < dimension:
            if board[r_r][r_c] != symbol:
                won = False
                break
            r_r += 1
            r_c -= 1

        return won