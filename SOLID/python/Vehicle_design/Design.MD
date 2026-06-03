Abstract Class Vehicle ->
attributes:
    name string
    top_speed float
    cur_speed float
    weight float

methods:
    start()
    stop()
    turn()


Drivable Interface
    drive()

Flyable Interface
    fly()

Sailable Interface
    sail()

EnergySource Interface
    + refill()
    + consume()

class FuelTank implements EnergySource
    - capacity float
    - current_fuel float

class Battery implements EnergySource
    - capacity float
    - current_fuel float

Bike class Inherits from Vehicle, Implements Drive and Fuel Interface
    - energysource EnergySource
Car class Inherits from Vehicle, Implements Drive and Fuel Interface
    - energysource EnergySource
EV class Inherits from Vehicle, Implements Drive and Electric Interface
    - energysource EnergySource
Airplane class Inherits from Vehicle, Implements Fly and Fuel Interface
    - energysource EnergySource
Amphibious class Inherits from Vehicle, Implements Drive and Sail and Fuel Interface
    - energysource EnergySource
Bicycle class Inherits from Vehicle, Implements Drive Interface