a=input("Enter the value")
print("You've entered ...>>",a)

# Normally input will turn the value into string
b=input("Enter value for b  ")
c=input("Enter value for c  ")
print(b+c) # because input treated as string so it will concatenate the values of b and c




d=int(input("Enter value for d   "))
e=int(input("Enter value for e   "))
print(d+e) # Now input treated as integer because we have cast so it will sum the values of d and e, but it doesn't support float values ..

f=float(input("Enter value for d   "))
g=float(input("Enter value for e   "))
print(f+g) # now input treated as float because we have cast so it will sum the values of f and g.

h=eval(input("Enter the value for h... "))
i=eval(input("Enter the value for i...  "))
print(h+i)


# The main type casting (type conversion) functions available in Python:

# int() – Converts a value to an integer.
# float() – Converts a value to a floating-point number.
# str() – Converts a value to a string.
# bool() – Converts a value to a boolean (True or False).
# list() – Converts a value to a list.
# tuple() – Converts a value to a tuple.
# set() – Converts a value to a set.
# dict() – Converts a value to a dictionary (usually from an iterable of key-value pairs).
# frozenset() – Converts a value to a frozenset (an immutable set).
# complex() – Converts a value to a complex number.

# Example Usage

# int(): Converts to an integer.
x = int("123")

# float(): Converts to a float.
x = float("123.45")

# str(): Converts to a string.
x = str(123)

# bool(): Converts to a boolean.
x = bool(1)  # True

# list(): Converts to a list.
x = list("hello")  # ['h', 'e', 'l', 'l', 'o']

# tuple(): Converts to a tuple.
x = tuple([1, 2, 3])

# set(): Converts to a set.
x = set([1, 2, 3, 3, 4])  # {1, 2, 3, 4}

# dict(): Converts to a dictionary (from an iterable of key-value pairs).
x = dict([(1, 'a'), (2, 'b')])  # {1: 'a', 2: 'b'}

# frozenset(): Converts to a frozenset.
x = frozenset([1, 2, 3])  # frozenset({1, 2, 3})

# complex(): Converts to a complex number.
x = complex(2, 3)  # (2+3j)

# These functions are used for type conversion in Python when you need to change the data type of a value.



