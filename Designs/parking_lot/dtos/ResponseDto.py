from abc import ABC, abstractmethod
from .ResponseStatusDto import ResponseStatusDto

class ResponseDto(ABC):
    def set_response_status(self, status: ResponseStatusDto):
        self.__status = status

    def get_response_status(self):
        return self.__status