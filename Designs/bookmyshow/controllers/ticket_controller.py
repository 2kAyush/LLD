from models import Ticket
from services import TicketService


class TicketController:
    def __init__(self, ticket_service: TicketService):
        self.__ticket_service = ticket_service

    def book_ticket(self, show_id, show_seat_ids, user_id) -> Ticket:
        return self.__ticket_service.book_ticket(show_id, show_seat_ids, user_id)