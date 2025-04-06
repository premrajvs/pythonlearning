# Scenario: Handling a potential division by zero error.
try:
    numerator = 10
    denominator = 0 #try changing the value to 1 and see the results
    result = numerator / denominator
    print(result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
        print("Division successful.")
finally:
        print("This part is executed irrespective of the exception")