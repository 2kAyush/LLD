from typing import Dict
from models import Ticket

class TicketRepository:
    def __init__(self):
        self.__id_counter = 0
        self.__tickets: Dict[int, Ticket] = {}

    def save(self, ticket: Ticket) -> Ticket:
        self.__id_counter += 1
        ticket.set_id(self.__id_counter)
        self.__tickets[self.__id_counter] = ticket
        return ticket

    def update(self, id: int, ticket: Ticket) -> Ticket:
        self.__tickets[id] = ticket
        return ticket

    def get_parking_lot(self, id: int) -> Ticket:
        return self.__tickets.get(id)

    def get_all_parking_lots(self) -> Dict[int, Ticket]:
        return self.__tickets