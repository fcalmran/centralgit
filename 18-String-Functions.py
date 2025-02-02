s1="Tom and Jerry"
print(len(s1)) # runs without any error
#print(lower(s1)) # Gives an error ..



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

print(s1.title())
# Capitalizes every word's first letter.

s2="Welcome"
print(s2.find("l"))
print(s2.find('lc')) # basically it find the first letter occurane and print the result
print(s2.find('e',2)) # basically we are telling to find the letter after the index 2 ..
print(s2.find('z')) # when the desired letter doesn't exist it will return -1.

text = "Hello, welcome to Python programming!"
result = text.find("Pyjaan")
print(result)  # Output: -1

text = "Hello, welcome to Python programming!"
result = text.find("Python")
print(result)  # Output: 18

# The find() method is used to find the index of the first occurrence of a substring within a string. It returns -1 if the substring is not found.

# 1. Basic example:

text = "Hello, welcome to Python programming!"
result = text.find("Python")
print(result)  # Output: 18

# This finds the index of the substring "Python" in the string.

# 2. When substring is not found:

text = "Hello, welcome to Python programming!"
result = text.find("Java")
print(result)  # Output: -1
# If the substring is not found, find() returns -1.

# 3. Finding a substring with a specific start position:

text = "Hello, welcome to Python programming!"
result = text.find("o", 5)  # Start searching from index 5
print(result)  # Output: 8

# This starts the search for "o" from index 5 and finds the first occurrence at index 8.

# 4. Using find() in a loop to find multiple occurrences:

text = "ababa"
substring = "a"
index = text.find(substring)
while index != -1:
    print(f"Found '{substring}' at index {index}")
    index = text.find(substring, index + 1)

# This loop will print all occurrences of the substring "a" in the string "ababa".

# 5. Using find() with the end parameter (in Python 3.9 and later):

text = "Hello, welcome to Python programming!"
result = text.find("o", 0, 5)  # Searching from index 0 to index 5
print(result)  # Output: 4

# This restricts the search to a specific range, from index 0 to index 5.

# These are just a few examples! The find() method is quite useful for searching substrings in strings efficiently. Let me know if you want more examples!


# Question : 
# does the find method finds the position of the letter or the whole word if we specify ? like in the example # 1 you mentioned.


# The find() method in Python searches for the exact substring you specify, whether it's a single letter or a whole word. So in Example #1:

text = "Hello, welcome to Python programming!"
result = text.find("Python")
print(result)  # Output: 18

# Here, the method is searching for the substring "Python", and it returns the starting index of the whole word "Python", which is 18. 
# If you were to search for just a letter, like "o", it would return the index of the first occurrence of that letter.

# So, if you do:

python
Copy
result = text.find("o")
print(result)  # Output: 4

# It returns 4, which is the index of the first "o" in the string.

# Key point:
# If you search for a substring like "Python", it finds the whole word and returns the position of its first occurrence.
# If you search for a single character like "o", it finds the position of the first occurrence of that character.
# Would you like to explore further with a different example or scenario?


# Question: 
# Does the find support multiple words ?


# The find() method in Python does not directly support searching for multiple words at once. It only works with a single substring at a time. 
# However, you can still search for multiple words by using loops or combining multiple find() calls.

# Here are a couple of ways to search for multiple words in a string:

# 1. Using multiple find() calls:
# If you want to check for multiple words separately, you can use find() for each word:


text = "Hello, welcome to Python programming!"
words = ["Hello", "Python", "Java"]

for word in words:
    result = text.find(word)
    if result != -1:
        print(f"'{word}' found at index {result}")
    else:
        print(f"'{word}' not found")
# This will search for each word and print the index where it's found, or indicate that it’s not found.

# 2. Using find() for all words in a sentence (with a loop):
# If you want to find the position of the first occurrence of any of the words in a list:

text = "Hello, welcome to Python programming!"
words = ["Java", "Python", "Hello"]

# Loop through each word and find its position
for word in words:
    index = text.find(word)
    if index != -1:
        print(f"Found '{word}' at position {index}")
# This will print the first occurrence of each word from the list.

# 3. Using regular expressions for more advanced searching:
# For more flexibility, you can use Python's re (regular expression) module to search for multiple words at once. 
# Here's an example:


import re

text = "Hello, welcome to Python programming!"
words = ["Python", "programming", "Hello"]

# Create a regular expression pattern to search for any of the words
pattern = '|'.join(words)  # Create a pattern like "Python|programming|Hello"
matches = re.finditer(pattern, text)

# Print all matches
for match in matches:
    print(f"Found '{match.group()}' at position {match.start()}")
# This method will match any of the words in the list and give you their positions.

# Summary:
# The find() method only works with one word/substring at a time.
# To search for multiple words, you can either use a loop with multiple find() calls or use regular expressions for more advanced pattern matching.
    


