from .EmailNotification import EmailNotification
from .SMSNotification import SMSNotification

class MarketingEmailNotification(EmailNotification):
    def send_email(self, message):
        print("Sent marketing email: ", message)

class MarketingSMSNotification(SMSNotification):
    def send_sms(self, message):
        print("Sent marketing sms: ", message)