from Notification import Notification

class EmailNotification(Notification):
    def send(self, message):
        print("sent the email: ", message)