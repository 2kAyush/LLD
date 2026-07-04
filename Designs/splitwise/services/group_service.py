from models import Group
from repositories import GroupRepository

import time

class GroupService:
    def __init__(self, group_repository: GroupRepository):
        self.__group_repository = group_repository

    def create_group(self, name, admins, created_by, participants) -> Group:
        group = Group()
        group.name = name
        group.admins = admins
        group.created_by = created_by
        group.participants = participants
        group.create_time = time.time
        return self.__group_repository.save(group)