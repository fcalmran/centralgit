s1="Breaking Bad"

print(s1[0]) # using index for selective character picking....


print(s1[0],s1[1],s1[2],s1[3],s1[4],s1[5],s1[6],s1[7],s1[8],s1[9],s1[10])


print(s1[8:11]) # instead using each use range like this

print("Flag",s1[0::1]) # Specifying the whole string with the increement of 1

print("Flag",s1[0::2]) # Specifying the whole string with the increement of 2



print(s1[-3],s1[-2],s1[-1]) #Using index from backwards...

print(s1[-1::-1]) # Printing the whole string backwards 


# String Indexing:
# In Python, strings are ordered sequences of characters. This means you can access individual characters in a string using indices.

# Indexing starts at 0 for the first character.
# Negative indices start from -1 for the last character.
# Examples of Indexing:

my_string = "Hello, World!"

# Accessing individual characters using positive indices:
print(my_string[0])  # H (first character)
print(my_string[7])  # W (8th character)

# Accessing individual characters using negative indices:
print(my_string[-1])  # ! (last character)
print(my_string[-2])  # d (second to last character)

# String Slicing:
# Slicing allows you to extract a substring from a string. You can specify a start index, an end index, and a step.

# The syntax is:

# substring = my_string[start:end:step]
# start: The starting index (inclusive).
# end: The ending index (exclusive).
# step: The step between each index (optional).


my_string = "Hello, World!"

# Extracting a substring from index 0 to 5 (not including 5):
substring = my_string[0:5]
print(substring)  # Hello

# Slicing with a step (every second character):
substring = my_string[0:10:2]
print(substring)  # Hlo ol

# Slicing from the beginning to index 5 (not including 5):
substring = my_string[:5]
print(substring)  # Hello

# Slicing from index 7 to the end:
substring = my_string[7:]
print(substring)  # World!

# Slicing with negative indices (from the end of the string):
substring = my_string[-6:-1]
print(substring)  # World

# Reverse the string using slicing:
reversed_string = my_string[::-1]
print(reversed_string)  # !dlroW ,olleH

# Key Points:
# Positive indices count from the beginning of the string (0 is the first character).
# Negative indices count from the end of the string (-1 is the last character).
# Slicing allows you to extract a part of the string based on indices.
# If you don’t specify start, it defaults to the beginning of the string, and if you don’t specify end, it goes until the end of the string.


