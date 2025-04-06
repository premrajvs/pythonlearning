# Scenario: Using the math module for square root.
import math
# if you comment the above statement and run it, you will get, NameError: name 'math' is not defined
number = 16
sqrt_number = math.sqrt(number)
print(f"The square root of {number} is: {sqrt_number}")