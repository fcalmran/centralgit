# In Python, there are several built-in data types that are commonly used. Below is a list of these data types, along with examples for declaration, assignment,
# and printing values.

# 1. Integer (int)
# Whole numbers without a decimal point.

# Declaration and assignment
my_integer = 10

# Printing the value
print(my_integer)  # Output: 10


# 2. Floating Point (float)
# Numbers with a decimal point.

# Declaration and assignment
my_float = 3.14

# Printing the value
print(my_float)  # Output: 3.14

# 3. String (str)
# A sequence of characters enclosed in single, double, or triple quotes.

# Declaration and assignment
my_string = "Hello, World!"

# Printing the value
print(my_string)  # Output: Hello, World!


# 4. Boolean (bool)
# Represents either True or False.

# Declaration and assignment
my_boolean = True

# Printing the value
print(my_boolean)  # Output: True

# 5. List (list)
# An ordered collection of items that can be of different data types, enclosed in square brackets.

# Declaration and assignment
my_list = [1, 2, 3, "apple", 3.14]

# Printing the value
print(my_list)  # Output: [1, 2, 3, 'apple', 3.14]

# 6. Tuple (tuple)
# An ordered, immutable collection of items, enclosed in parentheses.

# Declaration and assignment
my_tuple = (1, 2, 3, "apple", 3.14)

# Printing the value
print(my_tuple)  # Output: (1, 2, 3, 'apple', 3.14)

# 7. Set (set)
# An unordered collection of unique items, enclosed in curly braces.

# Declaration and assignment
my_set = {1, 2, 3, 4}

# Printing the value
print(my_set)  # Output: {1, 2, 3, 4}


# 8. Dictionary (dict)
# An unordered collection of key-value pairs, enclosed in curly braces.

# Declaration and assignment
my_dict = {"name": "John", "age": 30}

# Printing the value
print(my_dict)  # Output: {'name': 'John', 'age': 30}

# 9. None Type (None)
# A special data type used to represent the absence of a value or a null value.

# Declaration and assignment
my_none = None

# Printing the value
print(my_none)  # Output: None


# 10. Complex Number (complex)
# A number with a real and an imaginary part, represented as a + bj.

# Declaration and assignment
my_complex = 3 + 4j

# Printing the value
print(my_complex)  # Output: (3+4j)

# These are the primary data types in Python. You can assign values to variables of these types, and use them in operations as required.



# Some More Examples of each data types

# Number Data Type
a=10
print(type(a),a)
a=2.5
print(type(a),a)
a=1+2j
print(type(a),a)

# String Data Type

s1="This is the most common string"
print(type(s1),s1)

s2='This is the example of single qoute string'
print(type(s1),s1)

s3 = '''
    Line 1 goes here...
    Line 2 goes here...
    Line 3 goes here...
    Line 4 goes here...
'''
print(type(s3),s3)

# List Data Type

list1 = [1,"two",3.0,'four']
print(type(list1), list1)

# Tuple Data Type
tpl1=(1,"two",3.5,'four')
print(type(tpl1),tpl1)

d={
 'course_name':'Python',
 'Duration': '2 Months',
 'Years':3

}

print(type(d),d)
print(d["course_name"])
print(d["Duration"])

st1={1,2,3,4,5}
print(type(st1),st1)

                                        # ORDERED & UNORDERED DATA TYPES

# In the context of Python data types, the terms ordered and unordered refer to the way elements are stored and accessed within a collection.

# 1. Ordered
# Definition: An ordered collection maintains the order of elements in which they were added. When you iterate over an ordered collection,
#  the elements will appear in the same order in which they were inserted.
# Data types that are ordered:
# List (list): Elements in a list are stored in the order they are added.
# Tuple (tuple): Similar to lists, tuples maintain the order of the elements.
# String (str): Strings are sequences of characters and maintain the order of characters.

# Example:

# List (ordered)
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Tuple (ordered)
coordinates = (10, 20, 30)
print(coordinates)  # Output: (10, 20, 30)
# In these cases, the order in which you add the elements to the collection is preserved.

# 2. Unordered
# Definition: An unordered collection does not guarantee that the order of elements is maintained. When you iterate over an unordered collection, 
# the order of elements may not be the same as the order in which they were added.
# Data types that are unordered:
# Set (set): Sets are unordered collections of unique elements. When you iterate over a set, the elements may not appear in the order you added them.
# Dictionary (dict): While dictionaries in Python 3.7+ maintain insertion order when you retrieve items, they are technically still unordered in terms of 
# how they manage their key-value pairs internally. However, this order is maintained during iteration.

#Example:


# Set (unordered)
fruits_set = {"apple", "banana", "cherry"}
print(fruits_set)  # Output might vary, e.g., {'banana', 'apple', 'cherry'}

# Dictionary (ordered in Python 3.7+ but traditionally unordered)
student = {"name": "Alice", "age": 25, "city": "New York"}
print(student)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Sets: The order of elements in the set may appear random when printed, as they don't maintain a specific order.
# Dictionaries (from Python 3.7 onwards) preserve the insertion order of keys when iterating, but they are not considered strictly ordered collections like lists or tuples.

# Summary of Ordered vs. Unordered:
# Ordered collections:
# List (list), Tuple (tuple), String (str)
# The order of elements is preserved (you get items in the same order you added them).
# Unordered collections:
# Set (set), Dictionary (dict—order-preserving in Python 3.7+ but not guaranteed in earlier versions)
# The order of elements is not guaranteed, especially for sets.

# In short:

# Ordered means the elements maintain their insertion sequence.
# Unordered means the elements do not guarantee to maintain any specific order when you access or iterate through them.



                                                # MUTABLE & IMMUTABLE DATA TYPES    

# In Python, mutable and immutable datatypes refer to whether the objects of a particular datatype can be changed (mutated) after they are created or not.

# Mutable Datatypes:

# Mutable datatypes are those whose values can be changed or modified after the object is created. In other words, you can modify the contents of the object without changing its identity (memory address).

# Examples of mutable datatypes:
# List: You can change the contents of a list, such as adding, removing, or modifying elements.


my_list = [1, 2, 3]
my_list[0] = 10  # Modifying the first element
my_list.append(4)  # Adding a new element

# Dictionary: You can add, remove, or modify key-value pairs in a dictionary.

my_dict = {'a': 1, 'b': 2}
my_dict['a'] = 10  # Modifying a value
my_dict['c'] = 3  # Adding a new key-value pair

# Set: You can add or remove elements from a set.

my_set = {1, 2, 3}
my_set.add(4)  # Adding an element
my_set.remove(2)  # Removing an element

# Bytearray: A mutable sequence of bytes.
my_bytearray = bytearray([1, 2, 3])
my_bytearray[0] = 10  # Modifying an element


# Immutable Datatypes:
# Immutable datatypes are those whose values cannot be changed after the object is created. If you try to modify an immutable object, a new object will be created instead.

# Examples of immutable datatypes:

# Tuple: You cannot modify the elements of a tuple once it is created.

my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # This will raise a TypeError

# String: You cannot change individual characters in a string. Any modification results in the creation of a new string.


my_string = "hello"
# my_string[0] = 'H'  # This will raise a TypeError
my_string = "Hello"  # Creating a new string object

# Frozenset: Like a set, but its elements cannot be modified.

my_frozenset = frozenset([1, 2, 3])
# my_frozenset.add(4)  # This will raise an AttributeError


# Bytes: Similar to bytearray, but immutable.

my_bytes = b'hello'
# my_bytes[0] = 10  # This will raise a TypeError

# Summary:
# Mutable types allow changes after creation (e.g., list, dict, set, bytearray).
# Immutable types do not allow changes after creation (e.g., tuple, str, frozenset, bytes).
# Understanding the difference between mutable and immutable types is important for managing data efficiently, especially when considering the effects of operations on these objects in terms of memory management and performance.
    