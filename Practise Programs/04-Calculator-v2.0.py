print(''' 
      -----------------------------------------
      Welcome to Python Simple Calculator v 2.0
      -----------------------------------------
            
      ------------------
      Operator Selection
      ------------------
      
      (+) Addition
      (-) Subtraction
      (*) Multiplication
      (/) Division
      (q) Quit
      ''')


# Defining Functions here.....
def sum(n1,n2):
 print("The Summation of the provided number is ... ",n1+n2)

def sub(n1,n2):
 print("The Subtraction of the provided number is ... ",n1-n2)

def mul(n1,n2):
 print("The Multiplication of the provided number is ... ",n1*n2)

def div(n1,n2):
 print("The MDivision of the provided number is ... ",n1/n2)

sel=input("Select the Options")
selected=sel.lower()

if selected=="addition" or selected=="subtraction" or selected=="multiplication" or selected=="division":
        n1=eval(input("Enter first number   "))
        n2=eval(input("Enter second number  "))
if selected=="addition":
        sum(n1,n2)
elif selected=="subtraction":
    sub(n1,n2)
elif selected=="multiplication":
    mul(n1,n2)
elif selected=="division":
    div(n1,n2)
else:
     print("You have entered wrong option, please run the program again and select the options mentioned in the Menu at startup") 
 
