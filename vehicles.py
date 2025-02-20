from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def move(self) -> None:
        pass


class Car(Vehicle):
    def move(self) -> None:
        print("Car is moving")


class Bicycle(Vehicle):
    def move(self) -> None:
        print("Bicycle is moving")


class TransportService:
    def transport(self, vehicle: Vehicle) -> None:
        vehicle.move()


if __name__ == "__main__":
    car = Car()
    bicycle = Bicycle()

    transport_service = TransportService()

    transport_service.transport(car)  # Output: Car is moving
    transport_service.transport(bicycle)  # Output: Bicycle is moving