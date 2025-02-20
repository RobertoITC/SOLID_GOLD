from abc import ABC, abstractmethod


# Interface defining the contract for any vehicle
class Vehicle(ABC):
    @abstractmethod
    def move(self) -> None:
        pass


# Concrete class Car implementing Vehicle interface
class Car(Vehicle):
    def move(self) -> None:
        print("Car is moving")


# Concrete class Bicycle implementing Vehicle interface
class Bicycle(Vehicle):
    def move(self) -> None:
        print("Bicycle is moving")


# TransportService depends on abstraction (Vehicle) rather than concrete classes
class TransportService:
    def transport(self, vehicle: Vehicle) -> None:
        vehicle.move()


# Example usage
if __name__ == "__main__":
    car = Car()
    bicycle = Bicycle()

    transport_service = TransportService()

    transport_service.transport(car)  # Output: Car is moving
    transport_service.transport(bicycle)  # Output: Bicycle is moving