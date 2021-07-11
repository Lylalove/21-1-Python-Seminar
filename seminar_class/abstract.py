# abc = abstract base class
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("The car is going")

    def stop(self):
        print("The car is stopped")

class MotorCycle(Vehicle):
    def go(self):
        print("The motorcycle is going")

    def stop(self):
        print("The motorcycle is stopped")

# vehicle = Vehicle()
car = Car()
motorcycle = MotorCycle()

# vehicle.go()
car.go()
motorcycle.go()

car.stop()
motorcycle.stop()