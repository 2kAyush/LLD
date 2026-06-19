from Enums import InkType

class Ink:
    def __init__(self, colour, type_: InkType, density):
        self.__colour = colour
        self.__type = type_
        self.__density = density

    def getColour(self):
        return self.__colour

    def getType(self):
        return self.__type

    def getDensity(self):
        return self.__density