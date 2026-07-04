from typing import Dict
from models import Ticket
class TicketRepository:
    def __init__(self):
        self.__id = 1
        self.__tickets: Dict[int: Ticket] = {}

    def save(self, ticket: Ticket) -> Ticket:
        ticket.set_id(self.__id)
        self.__tickets[self.__id] = ticket
        self.__id += 1
        return ticket

    def update(self, ticket_id: int, ticket: Ticket):
        self.__tickets[ticket_id] = ticket

    def get_ticket(self, ticket_id) -> Ticket:
        return self.__tickets[ticket_id]
