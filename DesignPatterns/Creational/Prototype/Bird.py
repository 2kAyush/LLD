from abc import abstractmethod
from Cloneable import Cloneable

class Bird(Cloneable):
    def __init__(self, name, height, weight):
        self.__name = name
        self.__height = height
        self.__weight = weight

    def get_name(self):
        return self.__name

    def get_height(self):
        return self.__height

    def get_weight(self):
        return self.__weight

    def about(self):
        print(self.__name, self.__height, self.__weight)

    @classmethod
    @abstractmethod
    def Clone(self):
        raise NotImplementedError("This have to be implemented in the child class")
