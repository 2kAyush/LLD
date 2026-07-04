from typing import Dict
from models import Group

class GroupRepository:
    def __init__(self):
        self.__id = 1
        self.__groups: Dict[int: Group] = {}

    def save(self, group: Group) -> Group:
        group.set_id(self.__id)
        self.__groups[self.__id] = group
        self.__id += 1
        return group

    def update(self, group_id: int, group: Group):
        self.__groups[group_id] = group

    def get_group(self, group_id) -> Group:
        return self.__groups[group_id]
