num = int(input("Enter the number here ... "))

if num <= 1:
    print("Not a Prime")
elif num == 2 or num == 3:
    print("The number is prime")
else:
    is_prime = True  # Assume the number is prime until proven otherwise
    for i in range(2, int(num**0.5) + 1):  # Check divisibility up to the square root of the number
        if num % i == 0:  # If divisible, it's not prime
            is_prime = False
            break  # No need to check further if we found a divisor
    if is_prime:
        print("The number is prime")
    else:
        print("Not a Prime")
