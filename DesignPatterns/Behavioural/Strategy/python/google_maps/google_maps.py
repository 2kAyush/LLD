from Enums.TransportMode import TransportMode
from strategy.pathCalculationStrategy import PathCalculationStrategy
from strategy.PathCalculationStrategyRegistry import PathCalculationStrategyRegistry

class GoogleMaps:
    def __init__(self, path_calculation_strategy_registry: PathCalculationStrategyRegistry):
        self.path_calculation_strategy : PathCalculationStrategy = None
        self.path_calculation_strategy_registry = path_calculation_strategy_registry

    def get_path_withoutStrategy(self, source, destination, transport_mode: TransportMode):
        # violates SRP and OCP.
        if transport_mode == TransportMode.CAR:
            print(f"Call {transport_mode} function")

        if transport_mode == TransportMode.BIKE:
            print(f"Call {transport_mode} function")

        if transport_mode == TransportMode.WALK:
            print(f"Call {transport_mode} function")

    def get_path_withStrategy(self, source, destination, transport_mode: TransportMode):
        # we can use factory and get object of path calculation strategy
        # but we don't need new objects so we will use registry
        self.path_calculation_strategy = self.path_calculation_strategy_registry.getstrategy(transport_mode)
        self.path_calculation_strategy.calculate_path(source, destination)