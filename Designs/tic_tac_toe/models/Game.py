from __future__ import annotations

from typing import List

from .Board import Board
from .Player import Player
from .Move import Move
from Enums import GameState, PlayerType
from strategies.winningStrategies import WinningStrategy
# import make move strategies (maybe)

class Game:
    def __init__(self):
        self.__board: Board  = None
        self.__players: List[Player] = []
        self.__gameState : GameState = GameState.NOT_STARTED_YET
        self.__winner: Player = None
        self.__last_player_idx: int = -1
        self.__winning_strategies = []
        self.__moves: List[Move] = []

    def get_winner(self) -> Player:
        return self.__winner

    def get_game_state(self) -> GameState:
        return self.__gameState

    def get_board(self) -> Board:
        return self.__board

    def set_board(self, dimension):
        self.__board = Board(dimension)

    def set_players(self, players : List[Player]):
        self.__players = players

    def set_win_strategies(self, winning_strategies: List[WinningStrategy]):
        self.__winning_strategies = winning_strategies

    def make_move(self):
        self.__last_player_idx = (self.__last_player_idx + 1) % len(self.__players)
        player = self.__players[self.__last_player_idx]
        move = player.make_move(self.__board)
        move.get_cell().set_symbol(move.get_symbol())
        self.__moves.append(move)

        for winning_strategy in self.__winning_strategies:
            if winning_strategy.check_win(move, self.__board):
                self.__winner =  player
                self.__gameState = GameState.WON
                # game should end
                return
        if len(self.__moves) == self.__board.get_dimension() ** 2:
            # draw
            self.__gameState = GameState.DRAW
            return

    def undo(self):
        if len(self.__moves) == 0:
            print("Can't undo as no moves made till now")
            # OR raise Exception
            return False
        last_move = self.__moves[-1]
        last_move.get_cell().empty_cell()

        # could be already 0 and 0 - 1 -> -1
        self.__last_player_idx = ((self.__last_player_idx + len(self.__players)) - 1) % len(self.__players)
        self.__moves.pop()
        return True

class GameBuilder:
    def __init__(self):
        self.players: List[Player] = []
        self.winning_strategies = []
        self.dimension = 3

    def set_players(self, players: List[Player]) -> GameBuilder:
        self.players = players
        return self

    def add_player(self, player: Player) -> GameBuilder:
        self.players.append(player)
        return self

    def set_winning_strategies(self, winning_strategy: List[WinningStrategy]) -> GameBuilder:
        self.winning_strategies = winning_strategy
        return self

    def add_winning_strategy(self, winning_strategy: WinningStrategy) -> GameBuilder:
        self.winning_strategies.append(winning_strategy)
        return self

    def set_dimension(self, dim) -> GameBuilder:
        self.dimension = dim
        return self

    def check_if_single_bot(self) -> bool:
        bot = 0
        for player in self.players:
            if player.get_player_type() == PlayerType.BOT:
                bot += 1
        return bot <= 1

    def build(self) -> Game:
        if not self.check_if_single_bot():
            # can raise exception here as well!.
            return None

        game = Game()
        game.set_board(self.dimension)
        game.set_players(self.players)
        game.set_win_strategies(self.winning_strategies)

        return game
