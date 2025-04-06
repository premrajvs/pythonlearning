# Let's say you want to do some task repeatedly. Instead of writing the same code over and over
# you can defne it as a method and call the method to perform the action many times
def add(x, y):
    return x + y

result = add(3, 5)
print(f"The sum is: {result}")
result = add(1, 2)
print(f"The sum is: {result}")