from dtos import (
    GenerateTicketRequestDto,
    GenerateTicketResponseDto,
    ResponseStatusDto
)

from services import TicketService
from models import Ticket

class TicketController:
    def __init__(self, ticket_service: TicketService):
        self.__ticket_service = ticket_service

    def generate_ticket(self, request: GenerateTicketRequestDto) -> GenerateTicketResponseDto:
        ticket = self.__ticket_service.generate_ticket(
            request.get_parking_lot_id(),
            request.get_vehicle(),
            request.get_spot_type(),
            request.get_entry_gate()
        )
        ticket_response = GenerateTicketResponseDto()
        ticket_response.set_ticket(ticket)
        ticket_response.set_response_status(ResponseStatusDto.SUCCESS)
        if not ticket:
            # ticket will already be set to None
            ticket_response.set_response_status(ResponseStatusDto.FAILURE)

        return ticket_response