from Pizza.Pizza import Pizza

class Cheese(Pizza):
    def __init__(self, pizza: Pizza = None):
        self.pizza = pizza

    def getCost(self):
        return 12 + self.pizza.getCost()

    def getConstituents(self):
        if self.pizza:
            return "Cheese " + self.pizza.getConstituents()