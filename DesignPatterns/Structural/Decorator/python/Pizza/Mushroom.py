from Pizza.Pizza import Pizza

class Mushroom(Pizza):
    def __init__(self, pizza: Pizza = None):
        self.pizza = pizza

    def getCost(self):
        return 11 + self.pizza.getCost()

    def getConstituents(self):
        if self.pizza:
            return "Mushroom " + self.pizza.getConstituents()