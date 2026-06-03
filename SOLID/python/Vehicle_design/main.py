from EnergyHandler import FuelTank, Battery

from Vehicles import Car, AirPlane, Amphibious, Bike, EVScooter

swift_fuel_tank = FuelTank(50, 20)
a380_fuel_tank = FuelTank(600, 300)
bike_fuel_tank = FuelTank(20, 10)
EV_Battery = Battery(100, 37)
amphibious_fuel_tank = FuelTank(300, 267)

swift = Car("swift", 100, 0, 350, swift_fuel_tank)
a380 = AirPlane("A380", 500, 0, 600, a380_fuel_tank)
apache = Bike("Apache200", 100, 0, 350, bike_fuel_tank)
amphibious = Amphibious("amph", 100, 0, 350, amphibious_fuel_tank)
ev_scooter = EVScooter("ola", 100, 0, 350, EV_Battery)

drivable_map = {"swift": swift, "apache": apache, "ev_scooter": ev_scooter, "amphibious": amphibious}
flyable_map = {"A380": a380}
sailable_map = {"amphibious": amphibious}

while True:
    print("input in the form: swift drive")
    ip = input().split()
    if ip[0] in drivable_map:
        obj = drivable_map[ip[0]]
        if ip[1] == "move":
            obj.drive()
    if ip[0] in sailable_map:
        obj = sailable_map[ip[0]]
        if ip[1] == "move":
            obj.sail()

    if ip[0] in flyable_map:
        obj = flyable_map[ip[0]]
        if ip[1] == "move":
            obj.fly()

    if ip[1] == "turn":
        obj.turn()

    elif ip[1] == "start":
        obj.start()
    elif ip[1] == "stop":
        obj.stop()

    obj.get_info()