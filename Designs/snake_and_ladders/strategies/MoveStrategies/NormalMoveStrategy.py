from typing import List
from .HandleMoveStrategy import HandleMoveStrategy
from strategies.diceUnlockStrategies import UnlockDiceStrategy
from models import Player, Board
from Enums import ButtonStatus

# can be named as get valid buttons strategy
# in other versions we can allow users to choose if a player can win
# if they cross the dimension as well
# e.g. if at 99 we can win if we get 4 as well(this can be moved to
# another strategy class then)

class NormalMoveStrategy(HandleMoveStrategy):
    def get_valid_buttons(self, dice_value:int, player: Player, board: Board, dice_unlock_strategy: UnlockDiceStrategy) -> List[int]:
        # check for overflow
        buttons = player.get_buttons()
        res = []
        for button in buttons:
            if button.get_status() == ButtonStatus.LOCKED:
                if dice_unlock_strategy.can_unlock(dice_value):
                    res.append(button.get_id())
            elif button.get_position() + dice_value <= board.get_dimension():
                res.append(button.get_id())
        return res