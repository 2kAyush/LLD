from abc import ABC, abstractmethod
from Notification.EmailNotification import EmailNotification
from Notification.SMSNotification import SMSNotification


class NotificationFactory(ABC):

    @abstractmethod
    def create_email_notification(self) -> EmailNotification:
        raise NotImplementedError

    @abstractmethod
    def create_sms_notification(self) -> SMSNotification:
        raise NotImplementedError