from EmailNotificationCreator import EmailNotificationCreator
from SMSNotificationCreator import SMSNotificationCreator

if __name__ == "__main__":
    sms_notif_creator = SMSNotificationCreator()
    sms_notif_creator.notify("Hi to number")

    email_notif_creator = EmailNotificationCreator()
    email_notif_creator.notify("Hi to mail")