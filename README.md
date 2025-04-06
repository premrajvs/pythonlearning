# pythonlearning

Repository to help learn Python programming in 100 days

# Assignments

**1. Variables and Data Types:**
Create variables named item_name, item_price, and in_stock. Assign appropriate values (a string, a float, and a boolean) to these variables representing an item in a store. Print the values of each variable.
Declare two integer variables, num1 and num2. Swap the values of these two variables without using a temporary variable. Print the values of num1 and num2 after the swap.
Create a list called student_grades containing three numerical grades. Calculate the average of these grades and store the result in a new variable average_grade. Print the average grade.

**2. Numbers (Integers, Floats):**
Write a program that takes the length and width of a rectangle as input (as floats) and calculates its area. Print the area formatted to one decimal place.
Calculate the perimeter of a circle given its radius (take the radius as input as an integer). Use math.pi for the value of pi. Print the perimeter.
Write code to determine if a given integer (take as input) is a multiple of 5. Print "Multiple of 5" or "Not a multiple of 5".

**3. Strings:**
Create a string variable containing a sentence. Write code to count the number of words in the sentence. Print the word count.
Given the string "programming", extract the substring "gram". Print the extracted substring.
Write a program that takes a word as input and checks if it ends with the letter 'g' (case-insensitive). Print True or False.

**4. Lists:**
Create a list of your three favorite colors. Add another color to the end of the list and then remove the second color from the list. Print the final list.
Given the list [10, 25, 5, 30, 15], write code to find the smallest number in the list. Print the smallest number.
Write a program that takes a list of numbers as input (separated by spaces) from the user and then prints the list in reverse order.

**5. Tuples:**
Create a tuple representing the coordinates of a point in 2D space (x, y). Print the individual x and y coordinates.
Given the tuple ("apple", "banana", "cherry", "date"), write code to find the index of the element "cherry". Print the index.
Write a program that creates a tuple containing the first five even numbers (2, 4, 6, 8, 10). Print the tuple.

**6. Dictionaries:**

Create a dictionary to store the capital cities of three countries (e.g., "USA": "Washington D.C."). Print the capital of one of the countries.
Given the dictionary {"name": "Alice", "age": 25}, write code to update the age to 26 and add a new key-value pair "city": "New York". Print the updated dictionary.
Write a program that takes a string as input and counts the frequency of each character in the string (ignoring spaces). Store the results in a dictionary and print it.

**7. Boolean Values (True, False):**
Declare two variables, is_student (boolean) and age (integer). Write a boolean expression that evaluates to True if the person is a student and their age is less than 30. Print the result.
Write code to check if a given number (take as input) is within the range of 10 to 20 (inclusive). Print True or False.
Declare a boolean variable has_license. Write a conditional statement that prints "Can drive" if has_license is True, and "Cannot drive" otherwise.

**8. Operators (Arithmetic, Comparison, Logical):**
Write a program that takes the base and height of a parallelogram as input and calculates its area. Print the area.
Write code that takes two numbers as input and checks if at least one of them is greater than 10. Print True or False.
Evaluate the expression 15 % 4 + 3 \* 2 \*\* 3 - 1. Write code to calculate and print the result.

**9. Input and Output (print(), input()):**
Write a program that prompts the user to enter their favorite programming language and then prints a message like "Your favorite programming language is [language]".
Write code that takes the price of an item and the quantity purchased as input from the user (as floats and integers, respectively). Calculate the total cost and print it with a clear message.
Write a program that asks the user for their name and age on separate lines and then prints a sentence combining this information.

**10. Conditional Statements (if, elif, else):**
Write a program that takes a number as input and prints whether it is even or odd.
Write a program that takes a student's grade (A, B, C, D, or F) as input and prints a corresponding message (e.g., "Excellent!", "Good", "Average", "Passing", "Failed").
Write a program that takes the current month as input (as a string) and prints the number of days in that month (you can assume February has 28 days for simplicity).

**11. Loops (for loop):**
Write a program that uses a for loop to print the numbers from 1 to 10.
Given the list ["apple", "banana", "cherry"], use a for loop to print each fruit in the list.
Write a program that uses a for loop to calculate the sum of all even numbers between 1 and 20 (inclusive).

**12. Loops (while loop):**
Write a program that uses a while loop to print the numbers from 10 down to 1.
Write a program that takes a number as input from the user and keeps prompting them to enter a positive number until they do so. Once a positive number is entered, print "Thank you!".
Write a program that uses a while loop to calculate the factorial of a given positive integer (take the integer as input).

**13. Functions (Defining and Calling):**
Define a function called greet that takes one argument (a name) and prints a greeting message like "Hello, [name]!". Call the function with your name as the argument.
Define a function called add_numbers that takes two numbers as arguments and returns their sum. Call the function with two different numbers and print the returned result.
Define a function called is_even that takes an integer as an argument and returns True if the number is even, and False otherwise. Call the function with a few different numbers and print the returned boolean values.

**14. Function Arguments and Return Values:**
Write a function called calculate_area that takes the length and width of a rectangle as arguments and returns its area. Call the function and print the returned area.  
Define a function called get_full_name that takes a first name and a last name as arguments and returns the full name as a single string. Call the function and print the result.
Write a function called double_list that takes a list of numbers as an argument and returns a new list where each number is doubled. Call the function with a sample list and print the returned list.

**15. Scope of Variables (Local vs. Global):**
Declare a global variable global_value = 10. Define a function that accesses and prints the value of global_value. Call the function.
Define a function that declares a local variable local_value = 5 and prints it. Try to access local_value outside the function and explain what happens.
Declare a global variable counter = 0. Define a function that increments the counter variable. Call the function multiple times and then print the final value of counter. (Hint: You might need the global keyword).

**16. Modules and Importing:**
Import the math module. Use the math.sqrt() function to calculate the square root of 25 and print the result.
Import only the pi constant from the math module. Calculate the area of a circle with a radius of 5 using this imported constant and print the result.
Create a simple Python file named my_module.py with a function inside it (e.g., a function that returns "Hello from my module!"). In another Python file, import this module and call the function, then print its return value.

**17. Basic File Handling (Reading):**
Create a text file named my_file.txt and write a few lines of text into it. Then, write a Python program that opens and reads the entire content of my_file.txt and prints it to the console.
Using the my_file.txt from the previous question, write a Python program that opens the file and reads it line by line, printing each line.
Write a Python program that opens my_file.txt, reads the first line, and prints it.

**18. Basic File Handling (Writing):**
Write a Python program that opens a new file named output.txt in write mode and writes the sentence "This is some text." into it.
Write a Python program that opens the output.txt file from the previous question in append mode and adds the line "Another line of text." to the end of the file.
Write a Python program that creates a list of three names and then writes each name to a new line in a file named names.txt. 19. String Formatting (f-strings):

Declare two variables, product = "Laptop" and price = 1200.99. Use an f-string to print a sentence like "The Laptop costs $1200.99."
Declare a variable temperature = 25.5. Use an f-string to print the temperature formatted to one decimal place, like "The temperature is 25.5°C."
Declare two variables, name = "Bob" and age = 30. Use an f-string to print a message with both variables, like "Bob is 30 years old." 20. Comments:

Write a short Python code snippet (e.g., a simple calculation) and add a single-line comment explaining what the code does.
Write a Python function and add a multi-line comment (docstring) at the beginning of the function explaining its purpose, arguments, and return value.
Go back to one of your previous Python programs and add comments to explain different parts of the code.

**19. List Comprehensions:**
Use a list comprehension to create a new list containing the squares of all numbers from 1 to 10. Print the new list.
Given the list ["apple", "banana", "cherry", "date"], use a list comprehension to create a new list containing only the fruits that start with the letter 'a'. Print the new list.
Use a list comprehension to create a list of even numbers between 20 and 30 (inclusive). Print the list.

**20. Dictionary Comprehensions:**
Use a dictionary comprehension to create a dictionary where the keys are numbers from 1 to 5 and the values are their squares. Print the dictionary.
Given the list ["apple", "banana", "cherry"], use a dictionary comprehension to create a dictionary where the keys are the fruits and the values are their lengths. Print the dictionary.
Use a dictionary comprehension to create a dictionary from the following two lists: keys = ["a", "b", "c"] and values = [1, 2, 3]. Print the dictionary.

**21. Sets and Set Operations:**
Create two sets, set1 = {1, 2, 3, 4, 5} and set2 = {4, 5, 6, 7, 8}. Write code to find and print their union.
Using the same sets from the previous question, write code to find and print their intersection.
Create a list [1, 2, 2, 3, 4, 4, 5]. Convert this list to a set to remove duplicate elements and then print the resulting set.

**22. Handling Exceptions (try, except, finally):**
Write a program that takes two numbers as input and attempts to divide the first by the second. Use a try-except block to handle the ZeroDivisionError if the second number is 0, and print an appropriate message.
Write a program that tries to open a file named "nonexistent_file.txt" in read mode. Use a try-except block to catch the FileNotFoundError and print a user-friendly message.
Write a program that attempts to open a file and read its contents. Use a try-except-finally block. In the try block, attempt the file operation. In the except block, handle a potential IOError. In the finally block, ensure that the file is closed, regardless of whether an exception occurred. (You'll need to simulate a file operation for this).

**23. Working with Files (Advanced - Different Modes, Context Manager):**
Write a program that opens a file named "data.txt" in write mode ('w') and writes the following lines to it: "First line\nSecond line\nThird line". Use a with statement (context manager) to ensure the file is automatically closed.
Write a program that opens the "data.txt" file from the previous question in read mode ('r') using a with statement and reads all the lines into a list. Print the list of lines.
Write a program that opens a file named "numbers.txt" containing numbers separated by spaces. Read all the numbers, convert them to integers, and calculate their sum. Use a with statement for file handling.
