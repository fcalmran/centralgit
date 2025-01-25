# While Loop.....
# Forward Loop...
i=1
while i<=10:
    print(i)
    i+=1

#Backward Loop
a=20
while a>=1:
    print(a)
    a=a-1


# Creating Table of any number supplied
numb=int(input("Enter the number...."))
j=1
while j<=10:
    print(numb,"x",j,"=",numb*j)
    j+=1




# In Python, the while loop is used for repeating a block of code as long as a specified condition is True. The general syntax is:


# while condition:
#     # code block

# 1. Basic while loop
# The most common use of a while loop is when you know the condition but not the number of iterations.

counter = 0
while counter < 5:
    print(counter)
    counter += 1

# In this case, the loop will print the numbers from 0 to 4.

# 2. Infinite loop
# If the condition is always True, you get an infinite loop. Be careful, as this can cause the program to hang.

while True:
    user_input = input("Type 'exit' to stop: ")
    if user_input == 'exit':
        break
# This keeps asking for input until the user types "exit".

# 3. while loop with else
# A while loop can have an else block, which executes when the loop ends without encountering a break.

count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("Loop finished without break.")
# Here, it will print 0, 1, 2 and then "Loop finished without break."


# 4. Using break to exit a loop
# You can use break to stop the loop based on a certain condition.

number = 0
while True:
    number = int(input("Enter a number (negative to stop): "))
    if number < 0:
        print("Negative number entered, exiting loop.")
        break
    print(f"You entered: {number}")
# This will keep asking for numbers and stop when the user enters a negative number.

# 5. Using continue to skip iterations
# continue allows you to skip the current iteration and move to the next one.

count = 0
while count < 5:
    count += 1
    if count == 3:
        continue  # Skip printing 3
    print(count)
# It will print 1, 2, 4, 5—skipping the print for 3.

# 6. while loop with a list
# You can use a while loop to iterate through a list by managing an index manually.

items = ["apple", "banana", "cherry"]
index = 0
while index < len(items):
    print(items[index])
    index += 1
# This prints each item in the list.

# 7. Using a while loop with a counter (timing or counting iterations)
# You can use a counter to stop the loop after a set number of iterations.

counter = 0
while counter < 3:
    print(f"Iteration {counter}")
    counter += 1
# This will print Iteration 0, Iteration 1, and Iteration 2.

# 8. Nested while loops
# You can also nest while loops within each other.

outer = 0
while outer < 3:
    inner = 0
    while inner < 2:
        print(f"Outer: {outer}, Inner: {inner}")
        inner += 1
    outer += 1
# This prints combinations of outer and inner loop values.

# 9. Using while for a countdown
# A countdown is another common application.

count = 5
while count > 0:
    print(count)
    count -= 1
print("Liftoff!")
# This will print numbers from 5 to 1, then "Liftoff!"

# These examples should give you a good overview of the versatility of the while loop in Python. 
# You can use it in a variety of situations depending on the problem you're solving! 

