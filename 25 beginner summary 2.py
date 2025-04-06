# 1. Variables and Data Types
result = None

# 2. Numbers (integers and floats for calculations)
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    # 10. Conditional Statements, 23. Handling Exceptions
    if num2 == 0:
        print("Error: Cannot divide by zero.")
        return "Error"
    return num1 / num2

# 12. Functions (Defining and Calling), 13. Function Arguments and Return Values
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

# 15. Modules and Importing
import datetime

# 16. Basic File Handling (Writing for logging)
def log_operation(operation, num1, num2, result):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] Operation: {num1} {operation} {num2} = {result}\n"
    try:
        with open("calculator_log.txt", "a") as log_file:
            log_file.write(log_entry)
    except IOError as e:
        print(f"Error writing to log file: {e}")

# 10. Loops (while loop), 19. String Formatting (f-strings), 9. Input and Output
while True:
    print("\nSimple Calculator:")
    print("Enter first number:")
    num1_str = input()
    print("Enter operation (+, -, *, /):")
    operation = input()
    print("Enter second number:")
    num2_str = input()

    # 23. Handling Exceptions, 2. Numbers
    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
        # 09. Conditional Statements, 6. Dictionaries
        if operation in operations:
            result = operations[operation](num1, num2)
            print(f"Result: {result}")
            log_operation(operation, num1, num2, result)
        else:
            print("Invalid operation.")
    except ValueError:
        print("Invalid number input. Please enter numeric values.")

    another = input("Perform another calculation? (yes/no): ")
    # 3. Strings
    if another.lower() != 'yes':
        break

# 3. Tuples (not directly used, but could store valid operations)
valid_operations = ('+', '-', '*', '/')