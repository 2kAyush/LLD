from IceCreamCone import *
from TextPrinter import *
from Pizza import *

def handle_icecream():
    orange_vanilla = VanillaScoop(VanillaScoop(OrangeCone()))
    print(orange_vanilla.getCost(), orange_vanilla.getConstituents())

    # let's say orange_vanilla is a base flavor and I want to add Butterscotch on top of it
    butter_orange_vanilla = ButterScotchScoop(orange_vanilla)
    print("butter_orange_vanilla :----")
    print(butter_orange_vanilla.getCost(), butter_orange_vanilla.getConstituents())

def handle_text():
    text = "Hello"

    final_text = Encrypt(Encode(PlainText(text)))

    print(final_text.getText())

def handle_Pizza():
    pizza = Paneer(Mushroom(Cheese(ThinCrust(ThinCrust()))))
    # pizza = Paneer(Mushroom(ThinCrust(Cheese(ThinCrust())))) # raise exception (as adding crust over toppings)
    print(pizza.getConstituents())
    print(pizza.getCost())

if __name__ == "__main__":
    handle_Pizza()