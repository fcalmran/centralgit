s1="Tom and Jerry"
print(len(s1)) # runs without any error
print(lower(s1)) # Gives an error ..



# lower(s1) gives error but if we use function like len(), it will not gives an error for example : 
# s1="Tom and Jerry"
# print(len(s1))

# Great question! You're absolutely right that using a function like len() works without any issue.
# The reason this works is that len() is a built-in Python function, not a method associated with the string object itself.

# Here’s a quick breakdown of the difference:

# len(): This is a built-in Python function that can be used on any iterable (including strings). 
# It works globally and doesn't need to be called as a method on the string object.


s1 = "Tom and Jerry"
print(len(s1))  # Output: 14

# lower(): This is a method that is specific to string objects, meaning it needs to be called on the string itself, like s1.lower(). 
# It is not a global function, and that's why you cannot call it like lower(s1)—you need to use it as a method on the string object.


s1 = "Tom and Jerry"
print(s1.lower())  # Output: "tom and jerry"

# So the key difference is:
# Functions like len() are global and can be used directly on a variable.
# Methods like lower() are attached to specific object types (like strings in this case) and must be called on an instance of that object.
