from NotificationFactory.NotificationFactory import NotificationFactory
from Notification.MarketingNotification import MarketingEmailNotification, MarketingSMSNotification


class MarketingNotificationFactory(NotificationFactory):

    def create_email_notification(self) -> MarketingEmailNotification:
        return MarketingEmailNotification()

    def create_sms_notification(self) -> MarketingSMSNotification:
        return MarketingSMSNotification()