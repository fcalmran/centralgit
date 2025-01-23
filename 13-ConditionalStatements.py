# Conditional statements in Python allow you to execute certain pieces of code based on whether a given condition is true or false. The primary conditional statements in Python are:

# if statement – This runs a block of code if the condition is true.
# else statement – This runs a block of code if the condition in the if statement is false.
# elif statement – This stands for "else if" and is used to check multiple conditions in sequence.
# Syntax:

# if condition:
#     # Code block executed if the condition is true
# elif another_condition:
#     # Code block executed if the first condition is false and the second one is true
# else:
#     # Code block executed if none of the conditions are true
# Examples:
# Example 1: Simple if statement

age = 20

if age >= 18:
    print("You are an adult.")
# Output:
# You are an adult.

# In this example, the message is printed only if the age is greater than or equal to 18.

# Example 2: Using if and else

# age = 16

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Output:


# You are a minor.
# Here, if the age is less than 18, the else block is executed.

# Example 3: Using if, elif, and else

temperature = 30

if temperature > 35:
    print("It's too hot!")
elif temperature > 20:
    print("It's a warm day.")
else:
    print("It's cold outside.")
# Output:

# It's a warm day.
# In this case, the program checks for the first condition (temperature > 35), then the second (temperature > 20), and executes the block of code for the condition that is true.

# Example 4: Nested conditional statements

x = 10
y = 20

if x > 5:
    if y > 10:
        print("Both conditions are true.")
    else:
        print("First condition is true, but second is false.")
else:
    print("First condition is false.")
# Output:

# Both conditions are true.

# This is an example of one conditional statement being nested inside another.

# Summary:
# if is used to check a condition and run code if it's true.
# else handles the case where the if condition is false.
# elif provides additional conditions to check if the if condition fails.
# These statements allow you to control the flow of your program based on different conditions.



# when to use multiple if statements instead of elif statements?


# In Python, you should use multiple if statements or elif statements depending on whether the conditions are mutually exclusive or independent. 
# Here's a breakdown of when to use each:

# 1. When to Use Multiple if Statements
# Independent conditions: Use multiple if statements when the conditions are not mutually exclusive and could all potentially be true at the same time.
#  Each if condition is evaluated independently, and multiple blocks of code could execute.

# Example:
temperature = 25
is_sunny = True

if temperature > 20:
    print("It's warm outside.")

if is_sunny:
    print("It's a sunny day.")

# Output:

# It's warm outside.
# It's a sunny day.
# In this case, both conditions are independent of each other. The temperature and sunshine conditions are checked separately, 
# and both can be true at the same time, so both code blocks are executed.

# 2. When to Use elif Statements
# Mutually exclusive conditions: Use elif when the conditions are mutually exclusive—that is, only one of the conditions can be true at a time.
#  Once a condition in the if or elif is satisfied, the rest of the conditions are skipped.

# Example:

temperature = 25

if temperature > 30:
    print("It's very hot!")
elif temperature > 20:
    print("It's warm.")
else:
    print("It's cold.")
# Output:

# It's warm.
# Here, only one condition will be true, and the rest will be skipped. Since the first condition is false, 
# the program checks the elif condition and executes that code block.

# Key Differences Between if and elif:
# Multiple if statements:

# Each condition is evaluated independently.
# Multiple conditions can be true, leading to multiple code blocks being executed.
# Use when you need to evaluate multiple conditions independently.
# elif statements:

# Once one condition is true, the rest of the conditions are ignored (skipped).
# Use when conditions are mutually exclusive, and only one block of code should execute.

# Example Scenario:
# Let's say you're checking whether someone is eligible for discounts based on age, membership, and whether they have a coupon.


age = 25
has_membership = True
has_coupon = False

# Using multiple 'if' statements (if conditions are independent)
if age > 18:
    print("Eligible for adult discount.")
if has_membership:
    print("Eligible for membership discount.")
if has_coupon:
    print("Eligible for coupon discount.")

# Output:

# Eligible for adult discount.
# Eligible for membership discount.

# Now, if these conditions are mutually exclusive and only one discount should apply, you would use elif:


age = 25
has_membership = True
has_coupon = False

# Using 'if' and 'elif' (conditions are mutually exclusive)
if age > 18:
    print("Eligible for adult discount.")
elif has_membership:
    print("Eligible for membership discount.")
elif has_coupon:
    print("Eligible for coupon discount.")

# Output:
# Eligible for adult discount.
# In this case, only one discount applies, and after the first condition is met, the rest are ignored.

# Summary:
# Multiple if statements: Use when conditions are independent and multiple blocks of code might be executed.
# elif statements: Use when conditions are mutually exclusive and only one block of code should execute.