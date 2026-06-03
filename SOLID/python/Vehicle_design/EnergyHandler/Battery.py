import time

from .EnergySource import EnergySource


class Battery(EnergySource):
    def __init__(self, capacity: float, current: float):
        self.capacity = capacity
        self.current_battery = current

    def refill(self, amount):
        print("starting to charge")
        self.current_battery = min(self.capacity, self.current_battery + amount)
        for _ in range(3):
            time.sleep(3)
            print("charging...")
        print("recharge done")

    def consume(self, amount: float):
        print("consuming battery: ", amount)
        self.current_battery = max(0, self.current_battery - amount)
        print("remaining battery: ", self.current_battery)

    def getRemainingEnergy(self) -> float:
        print("current Battery: ", self.current_battery)
        return self.current_battery