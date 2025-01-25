s1="The Game of Thrones"
s1=s1[-1::-1]
tmp=len(s1)
print(tmp)

for i in range(tmp):
    print(i,s1[i])

#direct printing
for a in s1:
    print(a)

# Iterating through each character using a for loop:

string = "Hello"
for char in string:
    print(char)

# 2. Using enumerate() to get both index and character:

string = "Python"
for index, char in enumerate(string):
    print(f"Index: {index}, Character: {char}")

# 3. Using a while loop to iterate through the string:

string = "Looping"
i = 0
while i < len(string):
    print(string[i])
    i += 1

# 4. Using list comprehension to create a list of characters:

string = "Comprehension"
chars = [char for char in string]
print(chars)

# 5. Using join() to combine characters into a string (for example, reversing the string):

string = "Reverse"
reversed_string = ''.join([char for char in reversed(string)])
print(reversed_string)

# These are just a few ways to iterate over strings in Python. Would you like more examples or explanations of any of these?


