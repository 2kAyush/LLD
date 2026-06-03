from .EmailNotification import EmailNotification
from .SMSNotification import SMSNotification

class TransactionalEmailNotification(EmailNotification):
    def send_email(self, message):
        print("Sent transactional email: ", message)

class TransactionalSMSNotification(SMSNotification):
    def send_sms(self, message):
        print("Sent transactional sms: ", message)