from abc import ABC, abstractmethod
from Enums import PlayerType
from .Symbol import Symbol
from .Board import Board

class Player(ABC):
    def __init__(self, name, player_type: PlayerType, symbol: Symbol):
        self.__name = name
        self.__player_type = player_type
        self.__symbol = symbol

    def get_name(self):
        return self.__name

    def get_player_type(self):
        return self.__player_type

    def get_symbol(self):
        return self.__symbol

    @abstractmethod
    def make_move(self, board: Board):
        """
            returns Move object
        """
        raise NotImplementedError