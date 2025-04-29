# Scenario: Printing each item in a list.
fruits = ["apple", "banana", "cherry"] # refer to program 4 to know about this collection
vegetables = ["carrot", "spinach", "radish"] # refer to program 4 to know about this collection

print("Approach 1")
for fruit in fruits:
    print(fruit)

print("Approach 2")
for i in range(len(fruits)):
    print(fruits[i])

print("Approach 3")
for i in range(1,len(fruits)):
    print(fruits[i])

print("Approach 4")
for i in range(1,len(fruits),2):
    print(fruits[i])

print("Approach 5")
for i,j in zip(fruits,vegetables):
    print(f"{i},{j}")

# example of comprehension - a simpler way to create a list or set or other collections
sentence = "the quick brown fox jumps over the lazy fox"
words = sentence.split()
#syntax for comprehension {expression for item in iterable if condition}
unique_lengths = {len(word) for word in words}
print(unique_lengths)