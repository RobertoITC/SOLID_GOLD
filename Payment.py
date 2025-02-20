from abc import ABC, abstractmethod
from typing import Dict, Optional
from datetime import datetime
from dataclasses import dataclass

@dataclass
class PaymentDetails:
    amount: float
    currency: str
    description: str
    transaction_id: str
    timestamp: datetime

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount: float, currency: str = "USD") -> PaymentDetails:
        """
        Process a payment with the specified amount and currency.
        
        Args:
            amount: The amount to process
            currency: The currency code (default: USD)
            
        Returns:
            PaymentDetails: Details of the processed payment
        """
        pass

    @abstractmethod
    def refund(self, transaction_id: str) -> bool:
        """
        Refund a specific transaction.
        
        Args:
            transaction_id: The ID of the transaction to refund
            
        Returns:
            bool: True if refund was successful, False otherwise
        """
        pass

    def get_status(self, transaction_id: str) -> str:
        """
        Get the status of a transaction.
        
        Args:
            transaction_id: The transaction ID to check
            
        Returns:
            str: The current status of the transaction
        """
        return "Processing"

class PayPalPayment(Payment):
    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.transactions: Dict[str, PaymentDetails] = {}

    def process_payment(self, amount: float, currency: str = "USD") -> PaymentDetails:
        # Aquí iría la lógica real de integración con PayPal
        transaction_id = f"PP_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        payment_details = PaymentDetails(
            amount=amount,
            currency=currency,
            description="PayPal payment",
            transaction_id=transaction_id,
            timestamp=datetime.now()
        )
        
        self.transactions[transaction_id] = payment_details
        print(f"Processing PayPal payment of {amount} {currency}")
        return payment_details

    def refund(self, transaction_id: str) -> bool:
        if transaction_id in self.transactions:
            print(f"Refunding PayPal transaction {transaction_id}")
            return True
        return False

class CreditCardPayment(Payment):
    def __init__(self, merchant_id: str, api_key: str):
        self.merchant_id = merchant_id
        self.api_key = api_key
        self.transactions: Dict[str, PaymentDetails] = {}

    def process_payment(self, amount: float, currency: str = "USD") -> PaymentDetails:
        # Aquí iría la lógica real de procesamiento de tarjeta de crédito
        transaction_id = f"CC_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        payment_details = PaymentDetails(
            amount=amount,
            currency=currency,
            description="Credit Card payment",
            transaction_id=transaction_id,
            timestamp=datetime.now()
        )
        
        self.transactions[transaction_id] = payment_details
        print(f"Processing Credit Card payment of {amount} {currency}")
        return payment_details

    def refund(self, transaction_id: str) -> bool:
        if transaction_id in self.transactions:
            print(f"Refunding Credit Card transaction {transaction_id}")
            return True
        return False

if __name__ == "__main__":
    # Crear instancias de pago
    paypal = PayPalPayment("client_id", "client_secret")
    credit_card = CreditCardPayment("merchant_id", "api_key")

    # Procesar pagos
    pp_payment = paypal.process_payment(100.00, "USD")
    cc_payment = credit_card.process_payment(50.00, "EUR")

    # Reembolsos
    paypal.refund(pp_payment.transaction_id)
    credit_card.refund(cc_payment.transaction_id)