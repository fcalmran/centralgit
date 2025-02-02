# Basic Print function in python...

# Using variables 
a=1
b=2
c,d,e = 3,4,5

print (a,b) 
print(c,d,e)
print(a+b+c+d+e)

# Dealing with string values...

print("Hello World")
print('12+5')
print('a+b+c+d+e')
print("Hello","World","Next Sentence Goes here")

# Dealing with standard conditions
print(1<10)


# 1. Basic Output:
# Use Case: Displaying simple messages or results to the user.

print("Hello, world!")


# 2. Debugging:
# Use Case: Checking the value of variables or the flow of the program.

x = 5
print(f"The value of x is: {x}")

# 3. Displaying Results:
# Use Case: Displaying the output of calculations or functions.

result = 10 + 20
print("The result is:", result)


# 4. Formatted Output:
# Use Case: Using f-strings or format() to display formatted strings.

name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")

# 5. Printing Multiple Variables:
# Use Case: Printing multiple variables or values in one line.

x, y = 3, 7
print(x, y)  # Output: 3 7


# 6. Printing Lists, Tuples, and Other Collections:
# Use Case: Displaying the contents of a list, tuple, or other collections.

my_list = [1, 2, 3, 4]
print(my_list)

# 7. Customizing End Character:
# Use Case: Modifying the end of the print output (e.g., without newline).

print("Hello", end=", ")
print("world!")

# 8. Printing in a Loop:
# Use Case: Printing output for each iteration in a loop.

for i in range(5):
    print(f"Iteration {i}")


# 9. Printing to a File:
# Use Case: Redirecting the output to a file instead of the console.

with open("output.txt", "w") as file:
    print("This is written to a file.", file=file)


# 10. Printing with Separator:
# Use Case: Printing items with a custom separator between them.

print("apple", "banana", "cherry", sep=", ")

# 11. Conditional Printing:
# Use Case: Displaying output conditionally based on some logic.

number = 10
if number > 5:
    print("The number is greater than 5.")

# 12. Interactive User Prompts:
# Use Case: Prompting users for input and displaying results.

name = input("Enter your name: ")
print(f"Hello, {name}!")

# 13. Printing Progress:
# Use Case: Indicating progress during long-running tasks.

for i in range(1, 11):
 print(f"Progress: {i*10}%", end="\r")

# 14. Printing JSON or Data Structures:
# Use Case: Pretty-printing JSON or complex data structures.

import json
data = {"name": "Alice", "age": 25}
print(json.dumps(data, indent=4))

# 15. Logging (Simple):
# Use Case: Basic logging functionality to trace code execution.

print("[INFO] Program started.")
print("[ERROR] Something went wrong!")

# 16. Printing Unicode and Special Characters:
# Use Case: Displaying characters from different languages or symbols.

print("Hello, 你好, Привет, مرحبا!")

# 17. Printing in a Readable Format for Complex Objects:
# Use Case: Printing complex objects like dictionaries in a more readable way.

data = {"name": "Alice", "age": 25, "location": "New York"}
print("User Info:", data)

# 18. Performance and Benchmarks (as a quick solution):
# Use Case: Printing time taken by certain operations for a quick performance check.

import time
start_time = time.time()
# Some long task
print(f"Task took {time.time() - start_time} seconds.")

# Conclusion:
# The print() function in Python is used for a wide range of purposes, including debugging, output formatting, user interaction,
#  and file writing. It's versatile and can be customized for different scenarios, making it an essential tool for both beginner and advanced Python programming.
