from controllers import UserController
from services import UserService
from repositories import UserRepository
from dtos import CreateUserRequestDto

if __name__ == "__main__":
    USER_REPOSITORY = UserRepository()
    USER_SERVICE = UserService(USER_REPOSITORY)
    USER_CONTROLLER = UserController(USER_SERVICE)

    user_request_dto = CreateUserRequestDto()
    user_request_dto.email = "abc@gmail.com"

    response = USER_CONTROLLER.create_user(user_request_dto)
    print(response.user)

    # create movie
    # create theatre, city, auditorium
    # add seats (payload audi_id, seat_map {seat_type: count} -> {VIP: 20, GOLD: 40,...})
    # create a show (show seats)
    # write logic for ticket booking
    # For all the above just need to write controllers, services and repositories \
    # Core logic of handling concurrent bookings is already handled in TicketService.book_ticket function