print(''' 
      -----------------------------------------
      Welcome to Python Simple Calculator v 1.0
      -----------------------------------------
            
      ------------------
      Operator Selection
      ------------------
      
      (+) for Addition
      (-) for Subtraction
      (*) for Multiplication
      (/) for Division

''')
operator=input("Please enter your desired operation  ")
if operator=="+" or operator=="-" or operator=="*" or operator=="/": # checking that entered operator is legit...
    print("You have selected"+" "+operator)
    print("Now, you have to enter desired numbers to perform "+" ", operator)

    n1=eval(input("Enter the first number  ")) # casting the inout 
    n2=eval(input("Enter the second number "))

    if operator=="+":
        print("The Result of ",operator," is ",n1+n2)
    elif operator=="-":
        print("The Result of ",operator," is ",n1-n2)
    elif operator=="*":
        print("The Result of ",operator," is ",n1*n2)
    elif operator=="/":
        print("The Result of ",operator," is ",n1/n2)
else: 
    print("You have entered the invalid Operator")
