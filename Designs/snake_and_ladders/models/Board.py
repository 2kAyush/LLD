import random

from typing import Dict
from ForeignEntities import *


class Board:
    def __init__(self, dimension: int):
        self.__dimension = dimension
        self.__entity_map : Dict[int, ForeignEntity] = {}
        # just to generate the entities in an efficient manner
        # should entities shouldn't be in the first or last position
        self.__valid_entity_positions = [i for i in range(2, dimension)]

    def generateEntities(self):
        snakes_count = random.randint(4, 7)
        ladders_count = random.randint(4, 7)
        for _ in range(snakes_count):
            a, b = random.choice(self.__valid_entity_positions), random.choice(self.__valid_entity_positions)
            snake = Snake(max(a, b), min(a, b))
            self.__entity_map[max(a, b)] = snake

        for _ in range(ladders_count):
            a, b = random.choice(self.__valid_entity_positions), random.choice(self.__valid_entity_positions)
            ladder = Ladder(min(a, b), max(a, b))
            self.__entity_map[min(a, b)] = ladder

        print("Generated entities:")
        for k, v in self.__entity_map.items():
            print(f"{v.get_type()} from {k} to {v.get_to()}")


    def get_final_move_position(self, position: int) -> int:
        if position in self.__entity_map:
            entity = self.__entity_map[position]
            print(f"You got into {entity.get_type()}")
            return entity.get_to()
        return position

    def get_dimension(self):
        return self.__dimension

    def add_foreign_entity(self, position, entity: ForeignEntity) -> bool:
        if position <= 1 or position > self.__dimension:
            return False
        self.__entity_map[position] = entity