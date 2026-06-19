from __future__ import annotations

from Pen.Pen import Pen
from Enums import Pentype
from Refil import RefilPen
from Refil import BallPenRefil

from strategies.writeStrategies import *

class Ballpen(Pen, RefilPen):

    def __init__(self, writeBehaviour: WriteBehaviour):
        self.refil: BallPenRefil = None
        self.can_change_refil = False
        super().__init__(Pentype.BALL, writeBehaviour)

    def getColour(self):
        return self.refil.getColour()

    def getRefil(self):
        return self.refil

    def canChangeRefil(self):
        return self.can_change_refil

    def changeRefil(self, refil):
        print("changed refil to", refil)


class BallPenBuilder:
    def setRefil(self, refil: BallPenRefil) -> BallPenBuilder:
        self.refil = refil
        return self

    def setCanChangeRefil(self, value) -> BallPenBuilder:
        self.can_change_refil = value
        return self

    def setWriteBehaviour(self, writeBehaviour) -> BallPenBuilder:
        self.writeBehaviour = writeBehaviour
        return self

    def set_name(self, name) -> BallPenBuilder:
        self.name = name
        return self

    def set_company(self, company) -> BallPenBuilder:
        self.company = company
        return self

    def set_price(self, price) -> BallPenBuilder:
        self.price = price
        return self

    def build(self) -> Ballpen:
        balllpen = Ballpen(self.writeBehaviour)
        balllpen.refil = self.refil
        balllpen.can_change_refil = self.can_change_refil
        self.set_name(self.name)
        self.set_company(self.company)
        self.set_price(self.price)
        return balllpen