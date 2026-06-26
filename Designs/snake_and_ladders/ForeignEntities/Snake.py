from .ForeignEntity import ForeignEntity
from Enums import EntityType

class Snake(ForeignEntity):
    def __init__(self, from_, to_):
        super().__init__(from_, to_, EntityType.SNAKE)
