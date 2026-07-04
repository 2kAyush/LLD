from .ResponseDto import ResponseDto
from models import Ticket

class GenerateTicketResponseDto(ResponseDto):

    def set_ticket(self, ticket: Ticket):
        self.__ticket = ticket

    def get_ticket(self):
        return self.__ticket
