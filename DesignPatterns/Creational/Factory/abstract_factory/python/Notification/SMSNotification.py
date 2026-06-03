from abc import ABC, abstractmethod

class SMSNotification(ABC):

    @abstractmethod
    def send_sms(self, message):
        raise NotImplementedError