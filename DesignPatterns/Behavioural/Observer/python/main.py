from Flipkart import Flipkart
from Subscriber.InvoiceManagementService import InvoiceManagementService
from order import Order

inv = InvoiceManagementService()
flipkart = Flipkart()

order = Order(123, 123)

flipkart.place_order(order)