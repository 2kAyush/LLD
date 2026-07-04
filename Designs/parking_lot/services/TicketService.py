from repositories import TicketRepository, ParkingLotRepository

from Enums import SpotType
from models import Vehicle, EntryGate, Ticket

from strategies.spotassignmentstrategy import SpotAssignmentStrategy

class TicketService:
    def __init__(
            self,
            ticket_repository: TicketRepository,
            spot_assignment_strategy: SpotAssignmentStrategy,
            parking_lot_repository: ParkingLotRepository
        ):
        self.__spot_assignment_strategy = spot_assignment_strategy
        self.__ticket_repository = ticket_repository
        self.__parking_lot_repository = parking_lot_repository

    def generate_ticket(
            self,
            parking_lot_id: int,
            vehicle: Vehicle,
            spot_type: SpotType,
            entry_gate: EntryGate
        ):
        parking_lot = self.__parking_lot_repository.get_parking_lot(parking_lot_id)
        spot = self.__spot_assignment_strategy.assign_spot(spot_type, parking_lot, entry_gate)

        if not spot:
            return None

        ticket = Ticket()
        ticket.set_vehicle(vehicle)
        ticket.set_gate(entry_gate)
        ticket.set_parking_lot(parking_lot)
        ticket.set_parking_spot(spot)

        return self.__ticket_repository.save(ticket)