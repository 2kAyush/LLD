from Pizza.Pizza import Pizza

class ThinCrust(Pizza):
    def __init__(self, pizza: Pizza = None):
        self.pizza = pizza
        if self.pizza and (
            "Paneer" in self.pizza.getConstituents() or
            "Mushroom" in self.pizza.getConstituents() or
            "Cheese" in self.pizza.getConstituents()):
            raise Exception("Can't add crust over toppings")

    def getCost(self):
        if self.pizza:
            return 25 + self.pizza.getCost()
        return 25

    def getConstituents(self):
        if self.pizza:
            return "ThinCrust " + self.pizza.getConstituents()
        return "ThinCrust"