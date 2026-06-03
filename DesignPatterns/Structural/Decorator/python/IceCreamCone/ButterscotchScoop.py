from IceCreamCone.IceCreamCone import IceCreamCone

class ButterScotchScoop(IceCreamCone):

    def __init__(self, icecreamcone: IceCreamCone):
        self.icecreamcone = icecreamcone
        self.cost = 4
        self.constituents = "ButterScotchScoop"

    def getConstituents(self):
        return self.icecreamcone.getConstituents() +  ", " + self.constituents

    def getCost(self):
        return self.icecreamcone.getCost() + self.cost
