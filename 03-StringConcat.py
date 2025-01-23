# String Concatenation...

s1="Hello"
s2="World"

print(s1+s2)

print(s1+" "+s2)

# Remember if we use + sign between two integer values , it behaves differently

# c=20
# print(c+30)

# # but when we combine both i.e integer and string it gives an error..
# print(s1+c)


# GPT Explanation ....

# 1. Basic String Concatenation (Strings Only)
# In Python, you can concatenate strings using the + operator:


str1 = "Hello"
str2 = "World"
result = str1 + " " + str2  # Concatenating two strings with a space
print(result)  # Output: "Hello World"


# 2. Concatenating Strings with Other Data Types
# In Python, you cannot directly concatenate strings with non-strings (e.g., numbers, booleans) unless you explicitly convert them to strings using str():


str1 = "The answer is"
num = 42

#print(str1+" "+num) # This gives an error string can't concatenate with integer...
print(str1+" "+str(num)) # we convert the num integer into string by using str function
print(str1,num) # Alternatively we use , as a separator instead of using + sign...

# result = str1 + " " + str(num)  # Convert number to string
# print(result)  # Output: "The answer is 42"


# 3. Concatenating Booleans and Null Values
# Booleans and None (null) in Python can also be converted to strings for concatenation:


str2 = "The statement is"
boolean_value = True
#print(str2+" "+boolean_value) # It gives an error that it can't be concat with boolean values , so you need to convert to string
result = str2 + " " + str(boolean_value)  # Converting boolean to string
print(result)  # Output: "The statement is True"

null_value = None
#print(str2+" "+null_value) # It gives an error that it can't be concat with Null values , so you need to convert to string
result2 = str1 + " " + str(null_value)  # Converting None to string
print(result2)  # Output: "The statement is None"


# 4. Concatenating Arrays (or Lists) of Strings
# In Python, you can concatenate a list of strings using join():


words = ["Hello", "beautiful", "world"]
result = " ".join(words)  # Joins the list with spaces between words
print(result)  # Output: "Hello beautiful world"


# 5. String Concatenation Performance Considerations
# Python: Using + for string concatenation in a loop can be inefficient due to the creation of new string objects. It's better to use str.join() when concatenating many strings.


# Inefficient
result = ""
for word in words:
    result += word  # This is slow for many iterations

# Efficient
result = "".join(words)  # This is faster
