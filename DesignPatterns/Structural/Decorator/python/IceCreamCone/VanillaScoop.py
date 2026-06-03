from IceCreamCone.IceCreamCone import IceCreamCone

class VanillaScoop(IceCreamCone):

    def __init__(self, icecreamcone: IceCreamCone):
        self.icecreamcone = icecreamcone
        self.cost = 3
        self.constituents = "VanillaScoop"

    def getConstituents(self):
        return self.icecreamcone.getConstituents() +  ", " + self.constituents

    def getCost(self):
        return self.icecreamcone.getCost() + self.cost
