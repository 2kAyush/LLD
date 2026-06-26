from typing import List
from abc import ABC, abstractmethod
from models import Player, Board
from strategies.diceUnlockStrategies import UnlockDiceStrategy


class HandleMoveStrategy(ABC):
    @abstractmethod
    def get_valid_buttons(self, dice_value: int, player: Player, board: Board, dice_unlock_strategy: UnlockDiceStrategy) -> List[int]:
        raise NotImplementedError