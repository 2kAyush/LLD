from strategy import *
from google_maps.google_maps import GoogleMaps
from Enums.TransportMode import TransportMode

if __name__ == "__main__":
    path_calculation_strategy_registry = PathCalculationStrategyRegistry()
    path_calculation_strategy_registry.register(TransportMode.CAR, CarPathCalculationStrategy())
    path_calculation_strategy_registry.register(TransportMode.BIKE, BikePathCalculationStrategy())
    path_calculation_strategy_registry.register(TransportMode.WALK, WalkPathCalculationStrategy())
