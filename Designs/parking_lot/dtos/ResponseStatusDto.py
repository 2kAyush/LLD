from enum import Enum
from sre_parse import FAILURE, SUCCESS

class ResponseStatusDto(str, Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"