from .Symbol import Symbol
from .Player import Player
from .Cell import Cell

class Move:
    def __init__(self, cell: Cell, player: Player):
        self.__cell = cell
        self.__symbol = player.get_symbol()
        self.__player = player

    def set_player(self, player: Player):
        self.__player = player

    def get_player(self) -> Player:
        return self.__player

    def get_cell(self) -> Cell:
        return self.__cell

    def get_symbol(self) -> Symbol:
        return self.__symbol