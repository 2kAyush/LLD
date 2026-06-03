import time

from EnergyHandler import EnergySource
from movement import Flyable
from .Vehicle import Vehicle


class AirPlane(Vehicle, Flyable):
    def __init__(self, name: str, top_speed: float, cur_speed: float, weight: float, energy_source: EnergySource):
        self.name = name
        self.top_speed = top_speed
        self.cur_speed = cur_speed
        self.weight = weight
        self.energy_source = energy_source

    def start(self):
        print(f"starting the Airplane {self.name}...")
        time.sleep(2)
        print(f"started {self.name}...")

    def stop(self):
        print(f"stopping the Airplane {self.name}...")
        time.sleep(1)
        print(f"stopped {self.name}...")

    def turn(self):
        print(f"Turning the Airplane {self.name} will consume 5 units of fuel...")
        self.energy_source.consume(5)
        time.sleep(4)
        self._update_current_speed(-2)
        cur_fuel = self.energy_source.getRemainingEnergy()
        print(f"Turned {self.name}, fuel remaining: {cur_fuel}")

    def fly(self):
        print(f"Flying the Airplane {self.name} will consume 10 units of fuel...")
        self.energy_source.consume(20)
        self._update_current_speed(200)
        time.sleep(2)
        cur_fuel = self.energy_source.getRemainingEnergy()
        print(f"Flew {self.name}, fuel remaining: {cur_fuel}")

    def get_info(self):
        print(f"{self.name} moving at {self.cur_speed} having {self.energy_source.getRemainingEnergy()} fuel")