import time

from enums import ShowSeatState, TicketStatus
from models import Ticket
from repositories import TicketRepository, ShowSeatRespositry, UserRepository, ShowRepository

class TicketService:
    def __init__(
            self,
            ticket_repository: TicketRepository,
            show_seat_repository: ShowSeatRespositry,
            user_repository: UserRepository,
            show_repository: ShowRepository
        ):
        self.__ticket_repository = ticket_repository
        self.__show_seat_repository = show_seat_repository
        self.__user_repository = user_repository
        self.__show_repository = show_repository

    def book_ticket(self, show_id, show_seat_ids, user_id) -> Ticket:

        """
            This full function should be executed as a transaction
            to handle concurrent booking requests.
            With isolation level set to Serializable read
            select show_seats query should be run with for_update
        ->  select * from show_seats where id in (show_seat_ids) for update
        """

        # fetch show sheats
        show_seats = self.__show_seat_repository.get_by_id_in(show_seat_ids)
        # check if all the seats are available or not
        for show_seat in show_seats:
            if not show_seat.is_available():
                raise Exception(f"{show_seat.get_id()} seat is not available rn.")
        # lock the seats
        for show_seat in show_seats:
            show_seat.set_state(ShowSeatState.LOCKED)

        # return ticket object
        ticket = Ticket()
        user = self.__user_repository.get_user(user_id)
        show = self.__show_repository.get_show(show_id)
        ticket.set_booked_by(user)
        ticket.set_show(show)
        ticket.set_show_seats(show_seats)
        ticket.set_ticket_status(TicketStatus.PENDING)
        ticket.set_time_of_booking(time.time())
        return self.__ticket_repository.save(ticket)