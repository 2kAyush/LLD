from controllers import GameController
from Enums import GameStatus
from models import Player
from strategies.diceUnlockStrategies import NormalUnlockDiceStrategy
from strategies.MoveStrategies import NormalMoveStrategy

if __name__ == "__main__":

    # players
    player1 = Player(0, "Ayush", "Blue")
    player2 = Player(1, "Aman", "red")
    player3 = Player(2, "Jyoti", "Green")
    player4 = Player(3, "Piyush", "Yellow")

    dice_unlock_strategy = NormalUnlockDiceStrategy()
    move_strategy = NormalMoveStrategy()

    game_controller = GameController()
    player_list = [player1, player2, player3, player4]
    game = game_controller.create_game(100, 6, 4, player_list, dice_unlock_strategy, move_strategy)

    while game_controller.get_game_status(game) in (GameStatus.RUNNING, GameStatus.NOT_STARTED_YET):
        # game_controller.display(game)
        game_controller.make_move(game)

    # game_controller.display(game)

    if game_controller.get_game_status(game) == GameStatus.OVER:
        print("LeaderBoard: ")
        rank = 1
        for player in game_controller.get_leader_board(game):
            print(f"{rank}: {player.get_name()}")
            rank += 1