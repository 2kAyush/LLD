from dtos import CreateUserRequestDto, CreateUserResponseDto
from services import UserService

class UserController:
    def __init__(self, user_service: UserService):
        self.__user_service = user_service

    def create_user(self, request: CreateUserRequestDto) -> CreateUserResponseDto:
        user = self.__user_service.create_user(request.email)

        response = CreateUserResponseDto()
        response.user = user
        return response