from strategy.pathCalculationStrategy import PathCalculationStrategy

class BikePathCalculationStrategy(PathCalculationStrategy):
    def __init__(self):
        pass

    def calculate_path(self, source, destination)-> str:
        return f"Path calculated for Bike from {source} to {destination}"