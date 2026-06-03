from NotificationCreator import NotificationCreator
from EmailNotification import EmailNotification

class EmailNotificationCreator(NotificationCreator):
    def create_notification(self)-> EmailNotification:
        return EmailNotification()
