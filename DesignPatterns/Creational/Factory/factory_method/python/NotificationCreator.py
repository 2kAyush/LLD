from abc import ABC, abstractmethod
from Notification import Notification


class NotificationCreator(ABC):

    @abstractmethod
    def create_notification(self) -> Notification:
        raise NotImplementedError("Not implemented in child classes")

    def notify(self, message):
        notifier = self.create_notification()
        notifier.send(message)