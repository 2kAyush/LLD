from NotificationFactory import NotificationFactory, MarketingNotificationFactory, TransactionalNotificationFactory

def send_notifications(factory: NotificationFactory):
    email = factory.create_email_notification()
    email.send_email("Mail")

    sms = factory.create_sms_notification()
    sms.send_sms("sms")

marketing_factory = MarketingNotificationFactory()

send_notifications(marketing_factory)

transactional_factory = TransactionalNotificationFactory()
send_notifications(transactional_factory)