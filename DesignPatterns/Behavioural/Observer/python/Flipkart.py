from Enums.EventType import EventType
from order import Order

class Flipkart:
    subscribers = {}
    def __init__(self):
        pass

    def place_order(self, order: Order):
        print("Order placed successfully, will notify all the subscribers now")
        self.notify(EventType.ORDER_PLACED, order)

    @classmethod
    def register_subscriber(cls, event: EventType, subscriber):
        if event not in cls.subscribers:
            cls.subscribers[event] = []
        cls.subscribers[event].append(subscriber)

    def notify(self, event: EventType, order: Order):
        for subscriber in self.subscribers.get(event):
            subscriber.listen(order)