# Scenario: Converting a string to lowercase and checking if it contains a substring.
text = "Hello World"
lower_text = text.lower()
print(f"Lowercase text: {lower_text}")
if "world" in lower_text:
    print("The string contains 'world'.")