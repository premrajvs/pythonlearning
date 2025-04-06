# Scenario: A function to calculate the sum of any number of arguments.
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3))
print(sum_all(10, 20, 30, 40, 50))

# Scenario: A function to print key-value pairs passed as keyword arguments.
def print_info(**kvargs):
    for key, value in kvargs.items():
        print(f"{key}: {value}")

print_info(name="Grace", country="USA", occupation="Engineer")