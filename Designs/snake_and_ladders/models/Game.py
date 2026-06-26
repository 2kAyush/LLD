from __future__ import annotations

from Enums import ButtonStatus, GameStatus

from typing import List

from .Board import Board
from .Dice import Dice
from .Player import Player
from .Button import Button
from strategies.MoveStrategies import *
from strategies.diceUnlockStrategies import *


class Game:
    def __init__(self):
        self.__game_status: GameStatus = GameStatus.RUNNING
        self.__board: Board = None
        self.__dice: Dice = None
        self.__players : List[Player] = None
        self.__make_move_strategy: HandleMoveStrategy = None
        self.__dice_unlock_strategy: UnlockDiceStrategy = None
        self.__total_button_per_player: int = 4
        self.__leaderboad = []
        self.__last_player_move_idx = -1

    def set_board(self, dimension):
        self.__board = Board(dimension)
        # can be done inside the boards constructor as well!.
        # but doing here for future control
        self.__board.generateEntities()

    def get_leaderboard(self):
        return self.__leaderboad

    def set_dice(self, dice_max_num: int):
        self.__dice = Dice(dice_max_num)

    def get_game_status(self):
        return self.__game_status

    def set_total_button_per_player(self, n: int):
        self.__total_button_per_player = n

    def set_players(self, players: List[Player]):
        self.__players = players

    def set_make_move_strategy(self, strategy: HandleMoveStrategy):
        self.__make_move_strategy = strategy

    def set_dice_unlock_strategy(self, strategy: UnlockDiceStrategy):
        self.__dice_unlock_strategy = strategy

    def make_move(self):
        self.__last_player_move_idx = (self.__last_player_move_idx + 1) % len(self.__players)
        player = self.__players[self.__last_player_move_idx]
        button_map = player.get_button_map()
        reroll = True
        while reroll:
            input(f"{player.get_name()} your turn, Press Enter to roll the dice")
            dice_value = self.__dice.roll_dice()
            if dice_value != self.__dice.get_max_num():
                reroll = False
            print("Dice_value: ", dice_value)
            valid_buttons = self.__make_move_strategy.get_valid_buttons(
                dice_value,
                player,
                self.__board,
                self.__dice_unlock_strategy
            )
            if not valid_buttons:
                print("You can't move any pieces, moving to next player")
                # continue also will work here
                break
            print("Your button positions: ")
            for id in valid_buttons:
                print(f"id={id}, position={button_map[id].get_position()}, status={button_map[id].get_status()}")
            while True:
                button_id = int(input("enter valid id of the button you wish to move"))
                if button_id not in valid_buttons:
                    print("it's not valid")
                    continue
                button = button_map[button_id]
                if button.get_status() == ButtonStatus.LOCKED and self.__dice_unlock_strategy.can_unlock(dice_value):
                    button.set_position(1)
                    button.set_button_status(ButtonStatus.IN_GAME)
                    break
                move_position = button.get_position() + dice_value
                move_position = self.__board.get_final_move_position(move_position)
                print("Moving at position: ", move_position)
                if move_position == self.__board.get_dimension():
                    button.set_button_status(ButtonStatus.COMPLETED)
                button.set_position(move_position)
                break

        if player.get_playable_buttons() == 0:
            self.__leaderboad.append(player)
            self.__players.pop(self.__last_player_move_idx)
            if len(self.__players) == 1:
                self.__leaderboad.append(self.__players[0])
                self.__game_status = GameStatus.OVER


class GameBuilder:
    def __init__(self):
        self.__total_button_per_player: int = 4
        self.__players: List[Player] = []
        self.__dice_unlock_strategy: UnlockDiceStrategy = NormalUnlockDiceStrategy
        self.__move_strategy: HandleMoveStrategy = NormalMoveStrategy
        self.__dimension = 100

    def set_players(self, players: List[Player]) -> GameBuilder:
        self.__players = players
        return self

    def set_dimension(self, dimension: int) -> GameBuilder:
        self.__dimension = dimension
        return self

    def set_dice_max(self, dice_max_num: int) -> GameBuilder:
        self.__dice_max_num = dice_max_num
        return self

    def set_make_move_strategy(self, strategy: HandleMoveStrategy) -> GameBuilder:
        self.__move_strategy = strategy
        return self

    def set_total_button_per_player(self, n: int) -> GameBuilder:
        self.__total_button_per_player = n
        return self

    def set_dice_unlock_strategy(self, strategy: UnlockDiceStrategy) -> GameBuilder:
        self.__dice_unlock_strategy = strategy
        return self

    def validate(self) -> bool:
        # there should be atleast 2 players
        # dimension should be a perfect square
        if len(self.__players) < 2:
            print("There should be atleast 2 players for a game to start")
            return False

        if self.__dimension != int((self.__dimension ** 0.5)) ** 2:
            print("Dimension should be a perfect square")
            return False
        return True

    def build(self) -> Game:
        if not self.validate():
            return None

        for player in self.__players:
            player.set_buttons([Button(i) for i in range(self.__total_button_per_player)])
        game = Game()
        game.set_board(self.__dimension)
        game.set_dice(self.__dice_max_num)
        game.set_dice_unlock_strategy(self.__dice_unlock_strategy)
        game.set_make_move_strategy(self.__move_strategy)
        game.set_players(self.__players)
        return game