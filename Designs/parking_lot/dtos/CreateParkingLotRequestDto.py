class CreateParkingLotRequestDto:
    def __init__(self):
        self.address = None
        self.no_of_floors = None
        self.no_of_entry_gates = None
        self.no_of_exit_gates = None

    # getters and setters
    def get_address(self) -> str:
        return self.address

    def get_no_of_floors(self) -> int:
        return self.no_of_floors

    def get_no_of_entry_gates(self) -> int:
        return self.no_of_entry_gates

    def get_no_of_exit_gates(self) -> int:
        return self.no_of_exit_gates

    def set_address(self, address: str):
        self.address = address

    def set_no_of_floors(self, no_of_floors: int):
        self.no_of_floors = no_of_floors

    def set_no_of_entry_gates(self, no_of_entry_gates: int):
        self.no_of_entry_gates = no_of_entry_gates

    def set_no_of_exit_gates(self, no_of_exit_gates: int):
        self.no_of_exit_gates = no_of_exit_gates