from controllers import ParkingLotController, TicketController
from services import ParkingLotService, TicketService
from repositories import ParkingLotRepository, TicketRepository
from Enums import VehicleType, SpotType
from models import Vehicle
from dtos import (
    CreateParkingLotRequestDto,
    UpdateParkingLotRequestDto,
    GenerateTicketRequestDto,
    AddParkingSpotRequestDto
)
from strategies.spotassignmentstrategy import RandomSpotAssignmentStrategy

PARKING_LOT_REPOSITORY = ParkingLotRepository()
PARKING_LOT_SERVICE = ParkingLotService(PARKING_LOT_REPOSITORY)
PARKING_LOT_CONTROLLER = ParkingLotController(PARKING_LOT_SERVICE)

TICKET_REPOSITORY = TicketRepository()
RANDOM_SPOT_ASSIGNMENT_STRATEGY = RandomSpotAssignmentStrategy()
TICKET_SERVICE = TicketService(TICKET_REPOSITORY, RANDOM_SPOT_ASSIGNMENT_STRATEGY, PARKING_LOT_REPOSITORY)
TICKET_CONTROLLER = TicketController(TICKET_SERVICE)

def main():
    # shall we create a registry to store all the controllers and services and repositories?

    # create parking lot
    create_parking_lot_request_dto = CreateParkingLotRequestDto()
    create_parking_lot_request_dto.set_address("Address 1")
    create_parking_lot_request_dto.set_no_of_floors(1)
    create_parking_lot_request_dto.set_no_of_entry_gates(1)
    create_parking_lot_request_dto.set_no_of_exit_gates(1)
    response_dto = PARKING_LOT_CONTROLLER.create_parking_lot(create_parking_lot_request_dto)
    parking_lot = response_dto.get_parking_lot()
    print(parking_lot.__dict__, end="\n\n")
    print("--- spots: ", parking_lot.get_parking_floor_by_num(1).get_parking_spots())

    # update address
    update_parking_lot_request_dto = UpdateParkingLotRequestDto()
    update_parking_lot_request_dto.set_address("ABC")
    update_parking_lot_request_dto.set_parking_lot_id(1)
    update_response = PARKING_LOT_CONTROLLER.update_address(update_parking_lot_request_dto)
    parking_lot = update_response.get_parking_lot()
    print(parking_lot.__dict__, end="\n\n")

    # add parking spot
    add_parking_spot_request_dto = AddParkingSpotRequestDto()
    add_parking_spot_request_dto.set_floor_no(1)
    add_parking_spot_request_dto.set_parking_lot_id(1)
    add_parking_spot_request_dto.set_spot_type(SpotType.MEDIUM)

    add_parking_spot_response = PARKING_LOT_CONTROLLER.add_parking_spot(add_parking_spot_request_dto)
    print(add_parking_spot_response.get_parking_lot().__dict__, end="\n\n")
    print("--- spots: ", parking_lot.get_parking_floor_by_num(1).get_parking_spots())

    # create ticket
    create_ticket_request_dto = GenerateTicketRequestDto()
    create_ticket_request_dto.set_entry_gate(parking_lot.get_entry_gates()[0])
    create_ticket_request_dto.set_parking_lot_id(1)
    vehicle = Vehicle(VehicleType.MEDIUM, "test")
    create_ticket_request_dto.set_vehicle(vehicle)
    create_ticket_request_dto.set_spot_type(SpotType.MEDIUM)

    ticket_response = TICKET_CONTROLLER.generate_ticket(create_ticket_request_dto)
    print(ticket_response.get_ticket().__dict__, end="\n\n")

if __name__ == "__main__":
    main()
