from typing import List

from .Cell import Cell

class Board:
    def _generate_board(self):
        self.__board: List[List[Cell]] = [[] for _ in range(self.__dimension)]
        for i in range(self.__dimension):
            for j in range(self.__dimension):
                self.__board[i].append(Cell(i, j))

    def __init__(self, dimension: int):
        self.__dimension = dimension
        self._generate_board()

    def get_board(self) -> List[List[Cell]]:
        return self.__board

    def get_cell(self, row: int, col: int) -> Cell:
        return self.__board[row][col]

    def get_dimension(self) -> int:
        return self.__dimension

    def print_board(self):
        print("------------")
        for row in range(self.__dimension):
            print("|", end = " ")
            for col in range(self.__dimension):
                symbol = self.get_cell(row, col).get_symbol() or " "
                print(symbol + " | ", end="")
            print()
            print("------------")