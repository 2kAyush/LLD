from Enums import BotDifficultyLevel
from strategies.BotPlayingStrategies import *


class BotPlayingStrategyFactory:
    def __init__(self):
        pass

    def createBotPlayingStrategyForDifficutlyLevel(self, difficulty_level: BotDifficultyLevel) -> BotPlayingStrategy:
        if difficulty_level == BotDifficultyLevel.EASY:
            return EasyBotPlayingStrategy()

        if difficulty_level == BotDifficultyLevel.MEDIUM:
            return MediumBotPlayingStrategy()

        if difficulty_level == BotDifficultyLevel.HARD:
            return HardBotPlayingStrategy()