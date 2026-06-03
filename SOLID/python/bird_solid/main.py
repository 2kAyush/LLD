from birds.bird import Bird
from birds.crow import Crow
from birds.sparrow import Sparrow
from birds.pigeon import Pigeon
from birds.ostrich import Ostrich
from birds.penguin import Penguin

from flying_strategies.crow_sparrow_flying_strategy import CrowSparrowFlyingBehaviour

from interfaces.flyable import FlyableInterface

from typing import List

def call_fly(birds : List[FlyableInterface]):
    for bird in birds:
        bird.fly()

def main():
    csfb = CrowSparrowFlyingBehaviour()
    c = Crow("kauwa", 8, 3, csfb)
    p = Pigeon("kabutar", 4,2)
    s = Sparrow("goraiya", 7, 3, csfb)
    peng = Penguin("bagula", 20,20)
    o = Ostrich("shutur", 30,40)

    birds = [c, p, s, peng, o]
    for bird in birds:
        bird.eat()
        bird.make_sound()
    call_fly([c,p,s])


if __name__ == "__main__":
    main()
