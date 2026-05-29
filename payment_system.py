"""
This payment system implementation uses the strategy pattern
"""
from abc import ABC, abstractmethod

# Strategy interface
class PaymentStrategy(ABC):
    """Common interface for payment methods"""
    @abstractmethod
    def pay(self, amount):
        """Logic for completing the payment"""

# Concrete strategy class
class CreditCardPayment(PaymentStrategy):
    """Class to handle credit card payments"""
    def pay(self, amount):
        """Make payment with credit card"""
        print("Processing credit card payment...")
        # Enter details for credit card payment
        print("Enter credit card information")
        card_num = input("Please enter your card number:")

        print(f"Charging £{amount} to card {card_num}")

# Concrete strategy class
class PayPalPayment(PaymentStrategy):
    """Class to handle PayPal payments"""
    def pay(self, amount):
        """Make payment with PayPal"""
        print("Processing PayPal payment...")
        # Enter details for PayPal payment
        print("Enter PayPal information")
        email = input("Please enter your email:")

        print(f"Charging £{amount} to account {email}")

# Concrete strategy class
class CryptocurrencyPayment(PaymentStrategy):
    """Class to handle cryptocurrency payments"""
    def pay(self, amount):
        """Make payment with cryptocurrency"""
        print("Processing cryptocurrency payment...")
        # Enter details for cryptocurrency payment
        print("Enter cryptocurrency information")
        wallet_address = input("Please enter your wallet address:")

        print(f"Charging £{amount} to wallet {wallet_address}")

# Context class
class PaymentProcessor:
    """Class to handle the processing of a payment"""
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def process(self, amount):
        """Execute the payment"""
        self.strategy.pay(amount)

print("Welcome to the payment system")
print("Please select a payment method:")
print("1. Credit card")
print("2. PayPal")
print("3. Cryptocurrency")
method = input("Enter selection (number): ")

processor = None
if method == "1":
    processor = PaymentProcessor(CreditCardPayment())
elif method == "2":
    processor = PaymentProcessor(PayPalPayment())
elif method == "3":
    processor = PaymentProcessor(CryptocurrencyPayment())
else:
    print("Invalid selection")

if processor:
    try:
        payment_amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount")
    else:
        processor.process(payment_amount)
