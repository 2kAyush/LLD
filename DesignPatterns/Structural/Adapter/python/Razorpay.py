from payment_gateway import PaymentGateway

class RazorpayPaymentGatewayAdapter(PaymentGateway):
    def __init__(self):
        self.ctr = 0

    def PaybyCC(self, card_number, cvv, amount):
        print("calling razorpay payment by card api with", card_number, cvv, amount)
        return 123

    def CheckPaymentStatus(self, payment_id):
        self.ctr += 1
        print("calling razorpay check payment status api with", payment_id)
        if self.ctr == 3:
            self.ctr = 0
            return True
        return False
