import time

from .EnergySource import EnergySource


class FuelTank(EnergySource):
    def __init__(self, capacity: float, current: float):
        self.capacity = capacity
        self.current_fuel = current

    def refill(self, amount):
        print("starting to refuel")
        self.current_fuel = min(self.capacity, self.current_fuel + amount)
        for _ in range(2):
            time.sleep(2)
            print("refueling")
        print("refueling done")

    def consume(self, amount: float):
        print("consuming fuel: ", amount)
        self.current_fuel = max(0, self.current_fuel - amount)
        print("remaining fuel: ", self.current_fuel)

    def getRemainingEnergy(self) -> float:
        print("current Fuel: ", self.current_fuel)
        return self.current_fuel