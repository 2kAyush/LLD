from models import Show
from repositories import ShowRepository

class ShowService:
    def __init__(self, show_repository: ShowRepository):
        self.__show_repository = show_repository

    def create_show(self, name) -> Show:
        show = Show()
        show.set_name(name)
        return self.__show_repository.save(show)
