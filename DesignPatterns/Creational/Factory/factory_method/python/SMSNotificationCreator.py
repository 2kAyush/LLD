from NotificationCreator import NotificationCreator
from SMSNotification import SMSNotification

class SMSNotificationCreator(NotificationCreator):
    def create_notification(self)-> SMSNotification:
        return SMSNotification()
