from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start (self):
        pass

    @abstractmethod
    def stop(self):
        pass




class Car(Vehicle):
    def start(self):
        print("Car Started")


    def stop(self):
        print("Car Stopped")


class Bike(Vehicle):
    def start(self):
        print("Bike Started")


    def stop(self):
        print("Bike Stopped")


c = Car()
c.start()
c.stop()

b = Bike()
b.start()
b.stop()