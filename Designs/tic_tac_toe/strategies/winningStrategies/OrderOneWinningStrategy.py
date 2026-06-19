from models import Move, Board
from .WinningStrategy import WinningStrategy

class OrderOneWinningStrategy(WinningStrategy):

    def __init__(self):
        self.initialized = False

    def initialize(self, board: Board):
        self.initialized = True

        # this will have to be handled for undo as well!..
        # then for that this should be a part of Board class
        # otherwise it will defeat the purpose of strategy!..
        self.rowCharCounts = []
        self.colCharCounts = []
        self.ldiagCharCounts = {}
        self.rdiagCharCounts = {}

        dim = board.get_dimension()

        for _ in range(dim):
            self.rowCharCounts.append({})
            self.colCharCounts.append({})

    def check_win(self, move: Move, board: Board) -> bool:
        if not self.initialized:
            self.initialize(board)
        dimension = board.get_dimension()
        cell = move.get_cell()
        symbol = cell.get_symbol()

        row, col = cell.get_row(), cell.get_col()

        # row
        if symbol not in self.rowCharCounts[row]:
            self.rowCharCounts[row][symbol] = 0
        self.rowCharCounts[row][symbol] += 1

        # col
        if symbol not in self.colCharCounts[col]:
            self.colCharCounts[col][symbol] = 0
        self.colCharCounts[col][symbol] += 1

        # left diag
        if row == col:
            if symbol not in self.ldiagCharCounts:
                self.ldiagCharCounts[symbol] = 0
            self.ldiagCharCounts[symbol] += 1
            if self.ldiagCharCounts[symbol] == dimension:
                return True

        # right diag
        if row + col == dimension - 1:
            if symbol not in self.rdiagCharCounts:
                self.rdiagCharCounts[symbol] = 0
            self.rdiagCharCounts[symbol] += 1
            print("coming here", self.rdiagCharCounts)
            if self.rdiagCharCounts[symbol] == dimension:
                return True


        if (self.rowCharCounts[row][symbol] == dimension or self.colCharCounts[col][symbol] == dimension):
            return True
