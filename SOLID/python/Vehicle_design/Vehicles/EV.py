import time

from EnergyHandler import EnergySource
from movement import Drivable
from .Vehicle import Vehicle


class EVScooter(Vehicle, Drivable):
    def __init__(self, name: str, top_speed: float, cur_speed: float, weight: float, energy_source: EnergySource):
        self.name = name
        self.top_speed = top_speed
        self.cur_speed = cur_speed
        self.weight = weight
        self.energy_source = energy_source

    def start(self):
        print(f"starting the EVScooter {self.name}...")
        time.sleep(2)
        print(f"started {self.name}...")

    def stop(self):
        print(f"stopping the EVScooter {self.name}...")
        time.sleep(1)
        print(f"stopped {self.name}...")

    def turn(self):
        print(f"Turning the EVScooter {self.name} will consume 3 % of battery...")
        self.energy_source.consume(3)
        time.sleep(4)
        self._update_current_speed(-2)
        cur_battery = self.energy_source.getRemainingEnergy()
        print(f"Turned {self.name}, battery remaining: {cur_battery}")

    def drive(self):
        print(f"Flying the EVScooter {self.name} will consume 8 % of battery...")
        self.energy_source.consume(8)
        time.sleep(2)
        self._update_current_speed(6)
        cur_battery = self.energy_source.getRemainingEnergy()
        print(f"Drove {self.name}, battery remaining: {cur_battery}")

    def get_info(self):
        print(f"{self.name} moving at {self.cur_speed} having {self.energy_source.getRemainingEnergy()} battery")