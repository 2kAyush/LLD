from strategy.pathCalculationStrategy import PathCalculationStrategy

class CarPathCalculationStrategy(PathCalculationStrategy):
    def __init__(self):
        pass

    def calculate_path(self, source, destination)-> str:
        return f"Path calculated for car from {source} to {destination}"