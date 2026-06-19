from typing import List
from Enums import *
from models import *
from strategies.winningStrategies import *

class GameController:
    def __init__(self):
        pass

    def create_game(self, dimension, players: List[Player], winning_strategies: List[WinningStrategy]) -> Game:
        return (
            GameBuilder()
            .set_dimension(dimension)
            .set_players(players)
            .set_winning_strategies(winning_strategies)
            .build()
        )

    def make_move(self, game: Game):
        game.make_move()


    def undo(self, game: Game) -> bool:
        return game.undo()

    def get_winner(self, game: Game) -> Player:
        return game.get_winner()

    def get_game_status(self, game: Game) -> GameState:
        return game.get_game_state()

    def display(self, game: Game):
        game.get_board().print_board()