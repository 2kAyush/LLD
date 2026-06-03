from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def PaybyCC(self, card_number, cvv, amount) -> int:
        raise NotImplementedError

    @abstractmethod
    def CheckPaymentStatus(self, payment_id) -> bool:
        raise NotImplementedError