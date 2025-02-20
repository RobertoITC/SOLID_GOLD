# Gestión de Envíos y Seguimiento de Paquetes
 
from abc import ABC, abstractmethod

# Principio de Segregación
class Trackable(ABC):
    @abstractmethod
    def track(self):
        pass   

class Deliverable(ABC):
    @abstractmethod
    def deliver(self):
        pass

class Routable(ABC):
    @abstractmethod
    def route(self):
        pass

# Clases de Empleados
class DeliveryGuy(Deliverable):
    def deliver(self):
        print("I'm delivering packages.")

class RoutesSupervisor(Trackable, Routable):
    def track(self):
        print("I'm tracking various routes.")
    
    def route(self):
        print("I'm optimizing a route.")

class CustomerSupport(Trackable):
    def track(self):
        print("Im tracking the state of a shipped package.")
