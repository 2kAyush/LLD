from .UnlockDiceStrategy import UnlockDiceStrategy

class NormalUnlockDiceStrategy(UnlockDiceStrategy):
    def can_unlock(self, value: int) -> bool:
        return value in(1, 6)