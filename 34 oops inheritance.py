# Scenario: Creating a ElectricCar class that inherits from Car.
'''
Why & Where: Allows creating specialized classes based on general ones, reducing code duplication and establishing "is-a" relationships.
Real World: Creating different types of vehicles (Car, Truck, Motorcycle) from a base Vehicle class, defining various user roles (Admin, User, Guest) with shared functionalities.
'''
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}")

class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print(f"Battery Capacity: {self.battery_capacity} kWh")

my_electric_car = ElectricCar("Tesla", "Model 3", 75)
my_electric_car.display_info()