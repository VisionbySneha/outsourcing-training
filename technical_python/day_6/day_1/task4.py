class Vehicle:
    def start(self):
        print("Vehicle is starting")
    
    def stop(self):
        print("Vehicle is stopping")

class Bus(Vehicle):
    def route(self):
        print("Bus is following route number 5")

class Bike(Vehicle):
    def wheelie(self):
        print("Bike is doing a wheelie")

class Car(Vehicle):
    def music(self):
        print("Car is playing music")

# Create objects of all 3
bus = Bus()
bus.start()     # inherited
bus.route()     # own
bus.stop()      # inherited

print()

bike = Bike()
bike.start()    # inherited
bike.wheelie()  # own
bike.stop()     # inherited

print()

car = Car()
car.start()     # inherited
car.music()     # own
car.stop()      # inherited