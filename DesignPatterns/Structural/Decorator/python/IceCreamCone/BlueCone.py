from IceCreamCone.IceCreamCone import IceCreamCone

class BlueCone(IceCreamCone):

    def __init__(self):
        self.cost = 5
        self.constituents = "BlueCone"

    def getConstituents(self):
        return self.constituents

    def getCost(self):
        return self.cost
