from abc import ABC, abstractmethod

class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass

class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "US Spec")

class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "EU Spec")

class Vehicle(ABC):
    def __init__(self, make, model, spec):
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} ({self.spec}): Двигун запущено")

class Motorcycle(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} ({self.spec}): Мотор заведено")


# Використання
# Створення фабрик
us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

# Створення транспортних засобів через фабрики
vehicle1 = us_factory.create_car("Ford", "Mustang")
vehicle2 = eu_factory.create_motorcycle("BMW", "R1250")

# Запуск двигунів
vehicle1.start_engine()
vehicle2.start_engine()

