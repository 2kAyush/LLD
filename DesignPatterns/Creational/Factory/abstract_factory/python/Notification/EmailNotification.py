from abc import ABC, abstractmethod


class EmailNotification(ABC):

    @abstractmethod
    def send_email(self, message):
        raise NotImplementedError