# Identity Operators are is and is not

# The identity operators are used to compare the memory locations of two objects. The two identity operators are:

# is: Returns True if two objects refer to the same memory location (i.e., they are the same object).
# is not: Returns True if two objects refer to different memory locations (i.e., they are not the same object).

 #Examples
x=10
y=10
print(x is y)
print(x==y)
print(x is not y , x!=y)

print(id(x)) # finding the memory location of x
print(id(y)) # finding the memory location of y

# NOTE:

# In Python, x is y and x == y are not the same and serve different purposes. Let's break down the difference:

# 1. x == y (Equality Comparison):
# The == operator checks if the values of the two objects are the same.
# It doesn't care whether x and y refer to the same object in memory, just whether their contents are equal.
# 2. x is y (Identity Comparison):
# The is operator checks if x and y refer to the same object in memory, i.e., it compares the identity of the objects, not their values.

# Example:

x = 10
y = 10

print(x == y)  # Output: True (because both x and y have the same value, 10)
print(x is y)  # Output: True (in this case, Python optimizes memory for small integers, and both x and y refer to the same object in memory)

# Explanation:
# x == y: This checks whether the values of x and y are equal. Since both x and y are 10, the result is True.
# x is y: This checks whether x and y refer to the same object in memory. In the case of small integers (like 10), Python interns small integers, 
# meaning it reuses the same memory location for identical integer values, so both x and y refer to the same object, resulting in True.
# When x is y might differ from x == y:
# If the variables are objects or larger integers, they might hold the same value but still be distinct objects in memory.

# Example with lists
x = [1, 2, 3]
y = [1, 2, 3]

print(id(x),"Checks", x == y)  # Output: True (the lists have the same content)
print(id(y),"Checks", x is y)  # Output: False (x and y are two different objects in memory)

# Here:

# x == y is True because the lists have the same content.
# x is y is False because x and y are two different objects in memory, even though they contain the same elements.

# Key Differences:
# == checks value equality.
# is checks identity equality (whether two variables point to the same object in memory).


# Conclusion:
# x == y and x is y are not the same.
# == compares values.
# is compares memory addresses or whether they are the same object.
