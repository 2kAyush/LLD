import random

class Dice:
    def __init__(self, max_num: int):
        self.__max_num = max_num

    def roll_dice(self) -> int:
        return random.randint(1, self.__max_num)

    def get_max_num(self) -> int:
        return self.__max_num
