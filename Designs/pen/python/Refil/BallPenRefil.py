from Enums import RefilType

from .Ink import Ink
from .Nip import Nip
from Refil.Refil import Refil

class BallPenRefil(Refil):
    def __init__(self, ink: Ink, type_: RefilType, nip: Nip, total_ink: int):
        super().__init__(ink, type_, nip, total_ink)