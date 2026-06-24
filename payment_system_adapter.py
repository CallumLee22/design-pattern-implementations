"""
This payment system implementation uses the adapter pattern
"""

from abc import ABC, abstractmethod


class PaymentInterface(ABC):
    """Common interface for the payment system"""

    @abstractmethod
    def pay(self, amount):
        """Pay the specified amount."""


class LegacyCreditCardService:
    """Existing credit card service with incompatible interface"""

    def make_payment(self, card_number, amount):
        """Logic for making payment with credit card"""
        print("Legacy credit card service processing payment...")
        print(f"Charging £{amount} to card {card_number}")


class LegacyPayPalService:
    """Existing PayPal service with incompatible interface"""

    def send_payment(self, email_address, amount):
        """Logic for making payment with PayPal"""
        print("Legacy PayPal service processing payment...")
        print(f"Charging £{amount} to PayPal account {email_address}")


class LegacyCryptoService:
    """Existing crypto service with incompatible interface"""

    def transfer_funds(self, wallet_address, amount):
        """Logic for making payment with crypto"""
        print("Legacy cryptocurrency service processing payment...")
        print(f"Charging £{amount} to wallet {wallet_address}")


class CreditCardAdapter(PaymentInterface):
    """Adapter class that adapts the legacy credit card service to the common PaymentInterface"""

    def __init__(self, service: LegacyCreditCardService):
        self.service = service

    def pay(self, amount):
        print("Processing credit card payment...")
        card_num = input("Please enter your card number:")
        self.service.make_payment(card_num, amount)


class PayPalAdapter(PaymentInterface):
    """Adapter class that adapts the legacy PayPal service to the common PaymentInterface"""

    def __init__(self, service: LegacyPayPalService):
        self.service = service

    def pay(self, amount):
        print("Processing PayPal payment...")
        email = input("Please enter your PayPal email:")
        self.service.send_payment(email, amount)


class CryptocurrencyAdapter(PaymentInterface):
    """Adapter class that adapts the legacy crypto service to the common PaymentInterface"""

    def __init__(self, service: LegacyCryptoService):
        self.service = service

    def pay(self, amount):
        print("Processing cryptocurrency payment...")
        wallet_address = input("Please enter your wallet address:")
        self.service.transfer_funds(wallet_address, amount)


class PaymentProcessor:
    """Context class that uses a payment adapter"""

    def __init__(self, payment_method: PaymentInterface):
        self.payment_method = payment_method

    def process(self, amount):
        """Process payment"""
        self.payment_method.pay(amount)


print("Welcome to the payment system")
print("Please select a payment method:")
print("1. Credit card")
print("2. PayPal")
print("3. Cryptocurrency")
method = input("Enter selection: ")

processor = None
if method == "1":
    processor = PaymentProcessor(CreditCardAdapter(LegacyCreditCardService()))
elif method == "2":
    processor = PaymentProcessor(PayPalAdapter(LegacyPayPalService()))
elif method == "3":
    processor = PaymentProcessor(CryptocurrencyAdapter(LegacyCryptoService()))
else:
    print("Invalid selection")

if processor:
    try:
        payment_amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount")
    else:
        processor.process(payment_amount)
