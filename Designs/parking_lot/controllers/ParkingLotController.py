from dtos import (
    CreateParkingLotRequestDto,
    CreateParkingLotResponseDto,
    UpdateParkingLotRequestDto,
    UpdateParkingLotResponseDto,
    AddParkingSpotResponseDto,
    AddParkingSpotRequestDto,
    ResponseStatusDto
)
from models import ParkingLot, ParkingFloor, EntryGate, ExitGate, DisplayBoard
from services import ParkingLotService

class ParkingLotController:
    def __init__(self, parking_lot_service: ParkingLotService):
        self.__parking_lot_service = parking_lot_service


    # create a new parking lot
    def create_parking_lot(self, create_parking_lot_request_dto: CreateParkingLotRequestDto) -> CreateParkingLotResponseDto:
        parking_lot = ParkingLot()
        parking_floors = []
        entry_gates = []
        exit_gates = []
        for i in range(create_parking_lot_request_dto.get_no_of_floors()):
            parking_floors.append(ParkingFloor(i + 1))
        for i in range(create_parking_lot_request_dto.get_no_of_entry_gates()):
            entry_gates.append(EntryGate(DisplayBoard()))
        for i in range(create_parking_lot_request_dto.get_no_of_exit_gates()):
            exit_gates.append(ExitGate())
        parking_lot.set_address(create_parking_lot_request_dto.get_address())
        parking_lot.set_parking_floors(parking_floors)
        parking_lot.set_entry_gates(entry_gates)
        parking_lot.set_exit_gates(exit_gates)

        parking_lot = self.__parking_lot_service.create_parking_lot(parking_lot)
        response_dto = CreateParkingLotResponseDto()
        response_dto.set_parking_lot(parking_lot)
        response_dto.set_response_status(ResponseStatusDto.SUCCESS)
        return response_dto


    def update_address(self, request_dto: UpdateParkingLotRequestDto) -> UpdateParkingLotResponseDto:
        parking_lot = self.__parking_lot_service.update_address(request_dto.get_parking_lot_id(), request_dto.get_address())
        response_dto = UpdateParkingLotResponseDto()
        response_dto.set_parking_lot(parking_lot)
        response_dto.set_response_status(ResponseStatusDto.SUCCESS)
        return response_dto

    def add_parking_spot(self, request: AddParkingSpotRequestDto) -> AddParkingSpotResponseDto:
        parking_lot = self.__parking_lot_service.add_parking_spot(
            request.get_parking_lot_id(),
            request.get_floor_no(),
            request.get_spot_type()
        )
        responseDto = AddParkingSpotResponseDto()
        responseDto.set_parking_lot(parking_lot)
        responseDto.set_response_status(ResponseStatusDto.SUCCESS)
        if not parking_lot:
            responseDto.set_response_status(ResponseStatusDto.FAILURE)

        return responseDto