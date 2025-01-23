# 1. Basic Variable Assignment
# Use Case: Storing simple values (e.g., integers, floats, strings) in variables.

x = 10  # Integer
name = "Alice"  # String
pi = 3.14  # Float

# 2. Storing User Input
# Use Case: Capturing input from users and storing it in a variable for later use.

user_name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Input as integer

# 3. Multiple Variable Assignment
# Use Case: Assigning values to multiple variables in a single line.

a, b, c = 10, 20, 30

# 4. Swapping Values
# Use Case: Swapping values between two variables.

a, b = 5, 10
a, b = b, a  # Swap values

# 5. Dynamic Typing
# Use Case: Assigning variables without explicitly declaring their type (Python is dynamically typed).

x = 5        # x is an integer
x = "Hello"  # x is now a string

# 6. Storing Complex Data Types
# Use Case: Storing lists, dictionaries, tuples, sets, and other collections.

my_list = [1, 2, 3, 4]
my_dict = {"name": "Alice", "age": 25}
my_tuple = (1, 2, 3)
my_set = {1, 2, 3}


# 7. Using Variables in Expressions
# Use Case: Combining variables in mathematical or logical expressions.

a = 10
b = 5
result = a + b  # Expression using variables

# 8. String Concatenation
# Use Case: Concatenating strings stored in variables.

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # Concatenate strings

# 9. Variable Scope (Local vs Global)
# Use Case: Understanding how variables work within different scopes (global and local).

global_var = "I am global"  # Global scope

def my_function():
    local_var = "I am local"  # Local scope
    print(global_var)  # Access global variable inside function
    print(local_var)  # Access local variable inside function

# 10. Constants
# Use Case: Defining constant values that shouldn’t change during execution.

PI = 3.14159  # Conventionally, constants are in uppercase
MAX_SIZE = 100


# 11. Using Variables in Loops
# Use Case: Storing and updating values within loops.

total = 0
for i in range(1, 6):
    total += i  # Update variable during loop
print(total)  # Output: 15


# 12. Using Variables in Conditional Statements
# Use Case: Using variables to store conditions for if, elif, and else.

age = 20
if age >= 18:
    print("Adult")
else:
    print("Minor")

# 13. Function Parameters and Return Values
# Use Case: Passing variables as arguments to functions and returning results.

def greet(name):
    return f"Hello, {name}!"

user_name = "Alice"
greeting = greet(user_name)  # Passing variable to function
print(greeting)


# 14. Using Variables with Mathematical Operations
# Use Case: Storing intermediate results for complex calculations.

length = 5
width = 3
area = length * width  # Store result of multiplication


# 15. Storing Results of Functions
# Use Case: Storing the result of a function call for later use.

def add(a, b):
    return a + b

sum_result = add(3, 4)  # Store the result of the function call
print(sum_result)  # Output: 7


# 16. Using Variables in List Comprehensions
# Use Case: Storing the results of list comprehensions in variables.

numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]  # Store result of list comprehension
print(squares)  # Output: [1, 4, 9, 16, 25]

# 17. Storing Return Values in Dictionaries
# Use Case: Using variables as dictionary keys or values.

user_info = {}
name = "Alice"
age = 30
user_info[name] = age  # Use variable as dictionary key
print(user_info)

# 18. Tracking State in Object-Oriented Programming
# Use Case: Using variables to represent object states in classes.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog("Buddy", 5)  # Assigning variables in class instance


# 19. Using Variables in Loops for Accumulating Results
# Use Case: Accumulating or reducing values in a loop using variables.

product = 1
for i in range(1, 6):
    product *= i  # Multiply the variable with each iteration
print(product)  # Output: 120 (1*2*3*4*5)


# 20. Variable Length Arguments in Functions
# Use Case: Passing a variable number of arguments to a function using *args or **kwargs.

def print_numbers(*args):
    for num in args:
        print(num)

print_numbers(1, 2, 3, 4)  # Using variable-length arguments


# 21. Default Values for Function Parameters
# Use Case: Assigning default values to function parameters.

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()  # Uses default value
greet("Alice")  # Uses passed value


# 22. Using Variables for Temporary Storage
# Use Case: Temporary variables used for intermediate processing.

total = 0
num = 5
temp = total + num  # Temporary storage for intermediate result
total = temp  # Updating total with the intermediate result


# 23. Shallow and Deep Copying of Variables
# Use Case: Assigning variables by reference (shallow copy) or creating independent copies (deep copy).

import copy
original = [1, 2, 3]
shallow_copy = original  # Shallow copy (both point to the same object)
deep_copy = copy.deepcopy(original)  # Deep copy (independent copy)


# 24. Constant Variables Using Named Tuples
# Use Case: Using named tuples to represent constant-like objects.

from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p1 = Point(10, 20)


# 25. Type Annotations (Optional)
# Use Case: Indicating the expected type of a variable (optional but useful for clarity).

age: int = 30
name: str = "Alice"


# 26. Global Variables in Functions
# Use Case: Accessing and modifying global variables inside functions using global keyword.

count = 0  # Global variable

def increment():
    global count
    count += 1

increment()
print(count)  # Output: 1

# Conclusion:
# Variables in Python are fundamental to storing, processing, and manipulating data. They can be used in a variety of contexts, ranging from 
# simple assignments to more complex scenarios like function arguments, loops, and object-oriented programming. The dynamic typing, ease of use, 
# and flexibility of variables make them a cornerstone of Python programming.
