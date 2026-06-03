from strategy.pathCalculationStrategy import PathCalculationStrategy

class WalkPathCalculationStrategy(PathCalculationStrategy):
    def __init__(self):
        pass

    def calculate_path(self, source, destination)-> str:
        return f"Path calculated for Walking from {source} to {destination}"