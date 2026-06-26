from .ForeignEntity import ForeignEntity
from Enums import EntityType

class NextPrime(ForeignEntity):
    def __init__(self, from_, to_):
        super().__init__(from_, to_, EntityType.NEXT_PRIME)

    def get_to(self):
        self.__from
        return 1