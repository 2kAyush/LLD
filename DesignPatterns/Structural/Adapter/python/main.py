from Flipkart import Flipkart
from Razorpay import RazorpayPaymentGatewayAdapter

if __name__ == "__main__":
    flipkart = Flipkart(RazorpayPaymentGatewayAdapter())
    flipkart.do_payment(2343, 24234, 234324)