from NotificationFactory.NotificationFactory import NotificationFactory
from Notification.TransactionalNotification import TransactionalEmailNotification, TransactionalSMSNotification


class TransactionalNotificationFactory(NotificationFactory):

    def create_email_notification(self) -> TransactionalEmailNotification:
        return TransactionalEmailNotification()

    def create_sms_notification(self) -> TransactionalSMSNotification:
        return TransactionalSMSNotification()