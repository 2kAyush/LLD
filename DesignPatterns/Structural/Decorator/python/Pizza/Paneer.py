from Pizza.Pizza import Pizza

class Paneer(Pizza):
    def __init__(self, pizza: Pizza = None):
        self.pizza = pizza

    def getCost(self):
        return 15 + self.pizza.getCost()

    def getConstituents(self):
        if self.pizza:
            return "Paneer " + self.pizza.getConstituents()