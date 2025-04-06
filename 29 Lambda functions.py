
'''
Lambda Functions (Anonymous Functions):
Why & Where: Useful for concise, throwaway functions, often as arguments to higher-order functions like map, filter, sorted, or in GUI programming for simple event handlers.
Real World: Simplifying data transformations in ETL pipelines, defining quick sorting criteria based on specific object attributes, creating simple callbacks for button clicks.

This file contains code implementation showing how the same task can be done with regular function and anonymous function
'''
# Scenario: A function to add a constant value to each element of a list.

# Example using a regular (named) function:
def add_regular(a, b):
  """Adds two numbers and returns the result."""
  return a + b

# Using the regular function
num1 = 5
num2 = 3
sum_regular = add_regular(num1, num2)
print(f"Sum using regular function: {sum_regular}")

#############################################################################################

# Define the lambda function and assign it to a variable
add_anonymous = lambda a, b: a + b

# Using the anonymous function
num1_anon = 5
num2_anon = 3
sum_anonymous = add_anonymous(num1_anon, num2_anon)
print(f"Sum using anonymous function: {sum_anonymous}")

# To make it more concise, You can also use it directly without assigning it to a variable:
result_direct = (lambda a, b: a + b)(num1_anon, num2_anon)
print(f"Sum using direct anonymous function: {result_direct}")

'''
Understanding add_anonymous = lambda a,b: a + b:

lambda: Keyword indicating an anonymous function.
a, b: These are the arguments that the lambda function will take (separated by commas).
:: Separator between the arguments and the expression.
a + b: This is the single expression that the lambda function will evaluate and return.
add_anonymous = ...: We assign this anonymous function to the variable add_anonymous. Now, add_anonymous can be called like a regular function.
Using the assigned anonymous function:

sum_anonymous = add_anonymous(num1_anon, num2_anon): We call the anonymous function (referenced by add_anonymous) with the arguments 5 and 3.
Using the anonymous function directly:

result_direct = (lambda a, b: a + b)(10, 2):
We define the lambda function lambda a, b: a + b.
Immediately after the definition, we use parentheses (10, 2) to call this function and pass the arguments 10 and 2. The result (12) is then assigned to result_direct.
Comparison:

Regular Function: Has a name (add_regular), can contain multiple statements (though this example is simple), and is defined using def. It's generally more readable for complex logic and can be easily reused throughout your code using its name.

Anonymous Function (Lambda): Is defined without a formal name using lambda, is limited to a single expression that is implicitly returned, and is often used for concise, simple operations, especially as arguments to other functions. While you can assign a lambda function to a variable (giving it a name for practical purposes), its strength lies in its ability to be defined inline when needed.
'''

