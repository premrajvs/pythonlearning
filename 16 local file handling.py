# Scenario: Reading the contents of a text file.
with open("my_file.txt", "r") as file:
    content = file.read()
    print(content)
# (Assume 'my_file.txt' exists with some text)