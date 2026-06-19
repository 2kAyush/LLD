from __future__ import annotations

from Pen.Pen import Pen
from Enums import Pentype
from Refil import RefilPen
from Refil import GelPenRefil

from strategies.writeStrategies import *

class Gelpen(Pen, RefilPen):

    def __init__(self, writeBehaviour: WriteBehaviour):
        self.refil: GelPenRefil = None
        self.can_change_refil = False
        super().__init__(Pentype.GEL, writeBehaviour)

    def getColour(self):
        return self.refil.getColour()

    def getRefil(self):
        return self.refil

    def canChangeRefil(self):
        return self.can_change_refil

    def changeRefil(self, refil):
        print("changed refil to", refil)


class GelPenBuilder:
    def setRefil(self, refil: GelPenRefil) -> GelPenBuilder:
        self.refil = refil
        return self

    def setCanChangeRefil(self, value) -> GelPenBuilder:
        self.can_change_refil = value
        return self

    def setWriteBehaviour(self, writeBehaviour) -> GelPenBuilder:
        self.writeBehaviour = writeBehaviour
        return self

    def set_name(self, name) -> GelPenBuilder:
        self.name = name
        return self

    def set_company(self, company) -> GelPenBuilder:
        self.company = company
        return self

    def set_price(self, price) -> GelPenBuilder:
        self.price = price
        return self

    def build(self) -> Gelpen:
        gelpen = Gelpen(self.writeBehaviour)
        gelpen.refil = self.refil
        gelpen.can_change_refil = self.can_change_refil
        self.set_name(self.name)
        self.set_company(self.company)
        self.set_price(self.price)
        return gelpen