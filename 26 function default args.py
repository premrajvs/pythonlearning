# Scenario: A function to greet a person, with a default greeting.
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("David"))
print(greet("Eve", "Good morning"))