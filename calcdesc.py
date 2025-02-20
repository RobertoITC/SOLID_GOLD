from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, amount: float) -> float:
        pass

class NoDiscount(DiscountStrategy):
    def apply_discount(self, amount: float) -> float:
        return amount

class VIPDiscount(DiscountStrategy):
    def apply_discount(self, amount: float) -> float:
        return amount * 0.9  

class SeasonalDiscount(DiscountStrategy):
    def apply_discount(self, amount: float) -> float:
        return amount * 0.8  


class PaymentProcessor:
    def __init__(self, discount_strategy: DiscountStrategy):
        self.discount_strategy = discount_strategy
    
    def process_payment(self, amount: float):
        final_amount = self.discount_strategy.apply_discount(amount)
        print(f"Procesando pago de: ${final_amount:.2f}")


if __name__ == "__main__":
    amount = 100.0
    
    print("Pago sin descuento:")
    processor = PaymentProcessor(NoDiscount())
    processor.process_payment(amount)
    
    print("\nPago con descuento VIP:")
    processor = PaymentProcessor(VIPDiscount())
    processor.process_payment(amount)
    
    print("\nPago con descuento de temporada:")
    processor = PaymentProcessor(SeasonalDiscount())
    processor.process_payment(amount)
