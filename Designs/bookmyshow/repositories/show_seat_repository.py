from typing import Dict, List
from models import ShowSeat

class ShowSeatRespositry:
    def __init__(self):
        self.__id = 1
        self.__show_seats: Dict[int: ShowSeat] = {}

    def save(self, show_seat: ShowSeat) -> ShowSeat:
        show_seat.set_id(self.__id)
        self.__show_seats[self.__id] = show_seat
        self.__id += 1
        return show_seat

    def update(self, show_seat_id: int, show_seat: ShowSeat):
        self.__show_seats[show_seat_id] = show_seat

    def get_show_seat(self, show_seat_id) -> ShowSeat:
        return self.__show_seats[show_seat_id]

    def get_by_id_in(self, show_seat_ids: List[int]) -> List[ShowSeat]:
        res = []
        for id_ in show_seat_ids:
            if id_ in self.__show_seats:
                res.append(self.__show_seats[id_])
        return res
