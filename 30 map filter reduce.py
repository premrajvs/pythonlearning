'''
Map, Filter, and Reduce:
Why & Where: Promote functional programming style, often more readable and sometimes more efficient for certain operations 
on collections.
Real World: Data cleaning and transformation (e.g., converting units, filtering out invalid data), processing log files, 
performing calculations across large datasets.
'''

# Scenario (map): Squaring each number in a list.
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))
print(squares)

# Scenario (filter): Getting even numbers from a list.
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Scenario (reduce): Calculating the product of all numbers in a list.
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)