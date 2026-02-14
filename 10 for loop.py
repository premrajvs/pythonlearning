# Scenario: Printing each item in a list.
fruits = ["apple", "banana", "cherry"] # refer to program 4 to know about this collection
vegetables = ["carrot", "spinach", "radish"] # refer to program 4 to know about this collection



# example of comprehension - a simpler way to create a list or set or other collections
sentence = "the quick brown fox jumps over the lazy fox avscdfg"
words = sentence.split()
#syntax for comprehension {expression for item in iterable if condition}
unique_lengths = {len(word) for word in words}
print(unique_lengths)