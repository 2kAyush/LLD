import time

from payment_gateway import PaymentGateway

class Flipkart:
    def __init__(self, payment_gateway: PaymentGateway):
        self.payment_gateway = payment_gateway


    def do_payment(self, card_no, cvv, amount):
        transaction_id = self.payment_gateway.PaybyCC(card_no, cvv, amount)
        while not self.payment_gateway.CheckPaymentStatus(transaction_id):
            print("waiting for payment to be successfull...")
            time.sleep(1)
