from .Gate import Gate
from Enums import GateStatus, GateType

class ExitGate(Gate):
    # it should have gate repository and gate service but for now handling things here only
    __counter = 0
    def __init__(self):
        self.__counter += 1
        super().__init__(
            self.__counter,
            f"operator_{self.__counter}",
            GateType.ENTRY,
            GateStatus.OPEN
        )