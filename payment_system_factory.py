"""
This payment system implementation uses the factory pattern
"""

from abc import ABC, abstractmethod


class PaymentInterface(ABC):
    """Common interface for payment methods"""

    @abstractmethod
    def pay(self, amount):
        """Perform the payment transaction"""


class CreditCardPayment(PaymentInterface):
    """Concrete payment strategy for credit cards"""

    def pay(self, amount):
        print("Processing credit card payment...")
        print("Enter credit card information")
        card_num = input("Please enter your card number:")
        print(f"Charging £{amount} to card {card_num}")


class PayPalPayment(PaymentInterface):
    """Concrete payment strategy for PayPal"""

    def pay(self, amount):
        print("Processing PayPal payment...")
        print("Enter PayPal information")
        email = input("Please enter your email:")
        print(f"Charging £{amount} to account {email}")


class CryptocurrencyPayment(PaymentInterface):
    """Concrete payment strategy for cryptocurrency"""

    def pay(self, amount):
        print("Processing cryptocurrency payment...")
        print("Enter cryptocurrency information")
        wallet_address = input("Please enter your wallet address:")
        print(f"Charging £{amount} to wallet {wallet_address}")


# Abstract factory class
class PaymentCreator(ABC):
    """Abstract creator defining the factory method"""

    @abstractmethod
    def create_payment(self) -> PaymentInterface:
        """Factory method to create a payment strategy"""

    def process_payment(self, amount):
        """Use the factory method to create and execute a payment"""
        payment = self.create_payment()
        payment.pay(amount)


# Concrete factory classes
class CreditCardCreator(PaymentCreator):
    """Creator for credit card payments."""

    def create_payment(self) -> PaymentInterface:
        return CreditCardPayment()


class PayPalCreator(PaymentCreator):
    """Creator for PayPal payments"""

    def create_payment(self) -> PaymentInterface:
        return PayPalPayment()


class CryptocurrencyCreator(PaymentCreator):
    """Creator for cryptocurrency payments"""

    def create_payment(self) -> PaymentInterface:
        return CryptocurrencyPayment()


print("Welcome to the payment system")
print("Please select a payment method:")
print("1. Credit card")
print("2. PayPal")
print("3. Cryptocurrency")
method = input("Enter selection (number): ")

creator = None
if method == "1":
    creator = CreditCardCreator()
elif method == "2":
    creator = PayPalCreator()
elif method == "3":
    creator = CryptocurrencyCreator()
else:
    print("Invalid selection")
if creator:
    try:
        payment_amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount")
    else:
        creator.process_payment(payment_amount)
