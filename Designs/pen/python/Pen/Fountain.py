from __future__ import annotations

from Pen.Pen import Pen
from Enums import Pentype
from Refil import Ink
from strategies.writeStrategies import *

class FountainPen(Pen):

    def __init__(self, writeBehaviour: WriteBehaviour):
        self.ink: Ink = None
        super().__init__(Pentype.FOUNTAIN, writeBehaviour)

    def getColour(self):
        return self.ink.getColour()


class FountainPenBuilder:
    def setInk(self, ink: Ink) -> FountainPenBuilder:
        self.ink = ink
        return self

    def setWriteBehaviour(self, writeBehaviour) -> FountainPenBuilder:
        self.writeBehaviour = writeBehaviour
        return self

    def set_name(self, name) -> FountainPenBuilder:
        self.name = name
        return self

    def set_company(self, company) -> FountainPenBuilder:
        self.company = company
        return self

    def set_price(self, price) -> FountainPenBuilder:
        self.price = price
        return self

    def build(self) -> FountainPen:
        fountainPen = FountainPen(self.writeBehaviour)
        fountainPen.ink = self.ink
        self.set_name(self.name)
        self.set_company(self.company)
        self.set_price(self.price)
        return fountainPen