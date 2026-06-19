# from .BallPen import Ballpen
from .GelPen import GelPenBuilder
from .BallPen import BallPenBuilder
from .Marker import MarkerBuilder
from .Fountain import FountainPenBuilder

class PenFactory:

    @staticmethod
    def createGelPen() -> GelPenBuilder:
        return GelPenBuilder()

    @staticmethod
    def createBallPen() -> BallPenBuilder:
        return BallPenBuilder()

    @staticmethod
    def createFountainPen() -> FountainPenBuilder:
        return FountainPenBuilder()

    @staticmethod
    def createMarker() -> MarkerBuilder:
        return MarkerBuilder()