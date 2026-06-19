from __future__ import annotations

from Pen.Pen import Pen
from Enums import Pentype
from Refil import RefilPen
from Refil import MarkerRefil

from strategies.writeStrategies import *

class Marker(Pen, RefilPen):

    def __init__(self, writeBehaviour: WriteBehaviour):
        self.refil: MarkerRefil = None
        self.can_change_refil = False
        super().__init__(Pentype.MARKER, writeBehaviour)

    def getColour(self):
        return self.refil.getColour()

    def getRefil(self):
        return self.refil

    def canChangeRefil(self):
        return self.can_change_refil

    def changeRefil(self, refil):
        print("changed refil to", refil)


class MarkerBuilder:
    def setRefil(self, refil: MarkerRefil) -> MarkerBuilder:
        self.refil = refil
        return self

    def setCanChangeRefil(self, value) -> MarkerBuilder:
        self.can_change_refil = value
        return self

    def setWriteBehaviour(self, writeBehaviour) -> MarkerBuilder:
        self.writeBehaviour = writeBehaviour
        return self

    def set_name(self, name) -> MarkerBuilder:
        self.name = name
        return self

    def set_company(self, company) -> MarkerBuilder:
        self.company = company
        return self

    def set_price(self, price) -> MarkerBuilder:
        self.price = price
        return self

    def build(self) -> Marker:
        marker = Marker(self.writeBehaviour)
        marker.refil = self.refil
        marker.can_change_refil = self.can_change_refil
        self.set_name(self.name)
        self.set_company(self.company)
        self.set_price(self.price)
        return marker