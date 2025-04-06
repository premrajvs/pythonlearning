# Scenario: Writing a message to a text file.
with open("my_file.txt", "w") as file:
    file.write("This is some text written to the file.")