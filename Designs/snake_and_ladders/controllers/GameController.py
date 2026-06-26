from typing import List
from models import *
from strategies.diceUnlockStrategies import *
from strategies.MoveStrategies import *

class GameController:
    def __init__(self):
        pass

    def create_game(
            self,
            dimension: int,
            dice_max_num: int,
            total_button_per_player: int,
            players: List[Player],
            dice_unlock_strategy: UnlockDiceStrategy,
            move_strategy: HandleMoveStrategy
        ) -> Game:
        return(
            GameBuilder()
            .set_dimension(dimension)
            .set_dice_max(dice_max_num)
            .set_dice_unlock_strategy(dice_unlock_strategy)
            .set_make_move_strategy(move_strategy)
            .set_players(players)
            .set_total_button_per_player(total_button_per_player)
            .build()
        )

    def make_move(self, game: Game):
        game.make_move()

    def get_leader_board(self, game: Game)-> List[Player]:
        return game.get_leaderboard()

    def get_game_status(self, game: Game):
        return game.get_game_status()

    # def print_board():
    #     pass