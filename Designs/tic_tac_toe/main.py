from controllers import GameController
from Enums import PlayerType, BotDifficultyLevel, GameState
from models import HumanPlayer, BotPlayer,  Symbol
from strategies.winningStrategies import *

if __name__ == "__main__":
    dimension = 3
    p1 = HumanPlayer("Ayush", PlayerType.HUMAN, Symbol("X"))
    p2 = HumanPlayer("Aman", PlayerType.HUMAN, Symbol("O"))
    p3 = BotPlayer(PlayerType.BOT, Symbol("-"), BotDifficultyLevel.EASY)

    normal_winning_strategy = NormalWinningStrategy()
    corner_winning_strategy = CornerWinningStrategy()
    order_one_winning_strategy = OrderOneWinningStrategy()
    # overall object of gamecontroller will be 1 throughout the runtime
    # We will just pass id of a game to the controller (here simply game object!..)
    game_controller = GameController()

    game = game_controller.create_game(
        dimension,
        [p1, p2, p3],
        # [normal_winning_strategy, corner_winning_strategy]
        [order_one_winning_strategy]
    )

    while game_controller.get_game_status(game) in (GameState.RUNNING, GameState.NOT_STARTED_YET):
        game_controller.display(game)
        game_controller.make_move(game)

    game_controller.display(game)

    if game_controller.get_game_status(game) == GameState.WON:
        print(f"{game_controller.get_winner(game).get_name()} has won")

    if game_controller.get_game_status(game) == GameState.DRAW:
        print(f"it's a Draw")