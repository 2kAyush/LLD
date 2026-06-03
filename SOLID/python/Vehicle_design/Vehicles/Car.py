import time

from EnergyHandler import EnergySource
from movement import Drivable
from .Vehicle import Vehicle


class Car(Vehicle, Drivable):
    def __init__(self, name: str, top_speed: float, cur_speed: float, weight: float, energy_source: EnergySource):
        self.name = name
        self.top_speed = top_speed
        self.cur_speed = cur_speed
        self.weight = weight
        self.energy_source = energy_source

    def start(self):
        print(f"starting the Car {self.name}...")
        time.sleep(2)
        print(f"started {self.name}...")

    def stop(self):
        print(f"stopping the Car {self.name}...")
        time.sleep(1)
        print(f"stopped {self.name}...")

    def turn(self):
        print(f"Turning the Car {self.name} will consume 1 units of fuel...")
        self.energy_source.consume(1)
        time.sleep(2)
        self._update_current_speed(-2)
        cur_fuel = self.energy_source.getRemainingEnergy()
        print(f"Turned {self.name}, fuel remaining: {cur_fuel}")

    def drive(self):
        print(f"Driving the Car {self.name} will consume 3 units of fuel...")
        self.energy_source.consume(3)
        self._update_current_speed(3)
        time.sleep(2)
        cur_fuel = self.energy_source.getRemainingEnergy()
        print(f"Drove {self.name}, fuel remaining: {cur_fuel}")

    def get_info(self):
        print(f"{self.name} moving at {self.cur_speed} having {self.energy_source.getRemainingEnergy()} fuel")