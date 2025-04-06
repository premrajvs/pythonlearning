# Scenario: Understanding the concept of class
'''
In basic level concepts, we went through many variable types that can hold data of one type.
Class is a data type that can hold a collection

Why & Where: Fundamental for structuring complex applications, promoting code reusability and maintainability.
Real World: Modeling real-world entities (users, products, orders), building frameworks and libraries, GUI development, game development.

'''
class Car:
    def __init__(self, make, model, color="black"):
        self.make = make
        self.model = model
        self.color = color

    def start_engine(self):
        print("Engine started!")

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Color: {self.color}")

another_car = Car("Honda", "Civic", "red")
another_car.display_info()
another_car.start_engine()

# Try making changes like removing self, remove _init method and see what happens