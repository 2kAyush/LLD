from Subscriber.Subscriber import Subscriber
from Flipkart import Flipkart
from Enums.EventType import EventType

class InvoiceManagementService(Subscriber):
    def __init__(self):
        Flipkart.register_subscriber(EventType.ORDER_PLACED, self)

    def listen(self, order):
        self.generateInvoiceforOrder(order)

    def generateInvoiceforOrder(self, order):
        print("generating invoice for order: ", order)