from IceCreamCone.IceCreamCone import IceCreamCone

class KesarPistaScoop(IceCreamCone):

    def __init__(self, icecreamcone: IceCreamCone):
        self.icecreamcone = icecreamcone
        self.cost = 5
        self.constituents = "KesarPistaScoop"

    def getConstituents(self):
        return self.icecreamcone.getConstituents() +  ", " + self.constituents

    def getCost(self):
        return self.icecreamcone.getCost() + self.cost
