from IceCreamCone.IceCreamCone import IceCreamCone

class OrangeCone(IceCreamCone):

    def __init__(self):
        self.cost = 2
        self.constituents = "OrangeCone"

    def getConstituents(self):
        return self.constituents

    def getCost(self):
        return self.cost
