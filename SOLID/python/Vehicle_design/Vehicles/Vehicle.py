from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self, name: str, top_speed: float, cur_speed: float, weight: float):
        self.name = name
        self.top_speed = top_speed
        self.cur_speed = cur_speed
        self.weight = weight

    @classmethod
    @abstractmethod
    def start(self):
        print("please implement this yourself!. Raising exception here.")
        raise NotImplementedError("Should be implemented by the child class")

    @classmethod
    @abstractmethod
    def stop(self):
        print("please implement this yourself!. Raising exception here.")
        raise NotImplementedError("Should be implemented by the child class")

    @classmethod
    @abstractmethod
    def turn(self):
        print("please implement this yourself!. Raising exception here.")
        raise NotImplementedError("Should be implemented by the child class")

    def _update_current_speed(self, diff):
        if self.cur_speed + diff <= 0:
            self.cur_speed = 0
        elif self.cur_speed + diff > self.top_speed:
            self.cur_speed = self.top_speed
        else :
            self.cur_speed += diff