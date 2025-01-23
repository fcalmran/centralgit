# Membership Operators are in , not in



# In Python, membership operators are used to test whether a value or variable is found in a sequence (such as a list, tuple, string, or set).
#  There are two membership operators:

# in: Returns True if the value is found in the specified sequence.
# not in: Returns True if the value is not found in the specified sequence.

# Examples
s1="Hello World"
print("H" in s1) # It basically just return true or false if the value exists or not
print("h" in s1)
print("World" in s1)

l1=[1,2,3,4,5]
print("Kaisa",5 in l1)

# Examples:
# 1. Using in operator:

# Example with a list
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # Output: True
print(6 in my_list)  # Output: False

# Example with a string
my_string = "Hello, World!"
print("Hello" in my_string)  # Output: True
print("Python" in my_string)  # Output: False

# 2. Using not in operator:

# Example with a tuple
my_tuple = (10, 20, 30, 40)
print(25 not in my_tuple)  # Output: True
print(30 not in my_tuple)  # Output: False

# Example with a set
my_set = {1, 2, 3, 4, 5}
print(6 not in my_set)  # Output: True

# When using the in operator with a string in Python, it does not only check the first letter; it checks for the presence of the substring within the string.

# Example:

# Example 1: Check if a substring is in the string
my_string = "Hello, World!"
print("World" in my_string)  # Output: True (substring 'World' is found in the string)
print("hello" in my_string)  # Output: False (case-sensitive check, 'hello' is not the same as 'Hello')

# Example 2: Check if a single character is in the string
print("H" in my_string)  # Output: True (character 'H' is found in the string)
print("z" in my_string)  # Output: False (character 'z' is not found in the string)


# Key points:
# The in operator checks for any occurrence of the substring, not just the first character.
# It performs a case-sensitive check, so lowercase and uppercase characters are treated as different.
# So, it checks if the exact substring you're looking for appears anywhere in the string.

