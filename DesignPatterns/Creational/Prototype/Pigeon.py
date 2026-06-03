from __future__ import annotations
import copy

from Bird import Bird

class Pigeon(Bird):
    def __init__(self, name, height, weight, age):
        self.__age = age
        # age can be added in Bird as well but doing it here just to show that different class is required
        super().__init__(name, height, weight)

    def Clone(self) -> Pigeon:
        new_pigeon = Pigeon(self.get_name(), self.get_height(), self.get_weight(), self.__age)
        return new_pigeon
        # OR:
        # return copy.deepcopy(self)