from Notification import Notification

class SMSNotification(Notification):
    def send(self, message):
        print("sent the sms: ", message)