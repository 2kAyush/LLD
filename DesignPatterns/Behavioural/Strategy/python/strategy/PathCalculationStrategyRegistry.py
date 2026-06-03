from Enums.TransportMode import TransportMode
from pathCalculationStrategy import PathCalculationStrategy

class PathCalculationStrategyRegistry:
    def __init__(self):
        self.strategies = {}

    def register(self, mode: TransportMode, strategy: PathCalculationStrategy):
        self.strategies[mode] = strategy

    def getstrategy(self, mode: TransportMode) -> PathCalculationStrategy:
        return self.strategies[mode]