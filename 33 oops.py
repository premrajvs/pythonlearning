# Scenario: Understanding the concept of class
'''
In basic level concepts, we went through many variable types that can hold data of one type.
Class is a data type that can hold a collection

Why & Where: Fundamental for structuring complex applications, promoting code reusability and maintainability.
Real World: Modeling real-world entities (users, products, orders), building frameworks and libraries, GUI development, game development.

'''
class Car:
 #   make = ""
 #   model = ""
 #   color = ""
    
    def __init__(self, make, model, color="black"):
        self.make = make 
        self.model = model
        self.color = color

    def start_engine(self):
        print(f"{self.make} Engine {self.color} started!")

Car1 = Car("Honda", "Civic", "red") # creating an object instance of the type Class and setting the value of variables
Car1.start_engine()

Car2 = Car("Toyota", "Corolla", "white")
Car2.start_engine()

Car3 = Car("Volvo", "XC 60") # takes default value when no value is set
Car3.start_engine()

# Try making changes like removing self, remove _init method and see what happens