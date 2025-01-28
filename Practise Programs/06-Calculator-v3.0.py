# My efforts....

# class calc():

#     def __init__(self,n1,n2):
#         self.numb1=n1
#         self.numb2=n2

#     def addi(self):
#         print(f"The Addition of the provided number {self.numb1} {self.numb2} is ",self.numb1+self.numb2)
#         # return self.numb1+self.numb2

#     def subtr(self):
#         print(f"The Subtraction of the provided number {self.numb1} {self.numb2} is ",self.numb1-self.numb2)

#     def mult(self):
#         print(f"The Multiplication of the provided number {self.numb1} {self.numb2} is ",self.numb1*self.numb2)

#     def divi(self):
#         print(f"The Division of the provided number {self.numb1} {self.numb2} is ",self.numb1/self.numb2)    

# n1=eval(input("Enter first number  "))
# n2=eval(input("Enter second number "))

# O1 = calc(n1,n2)

# O1.addi()
# O1.subtr()
# O1.mult()
# O1.divi()

# print(f"The Addition of the provided number {n1} and {n2} is ...", O1.addi())

#-------------------------------------------------------------------------------------------------


# New Imporved Version provided by GPT

class calc:
    def __init__(self, n1, n2):
        self.numb1 = n1
        self.numb2 = n2

    def addi(self):
        print(f"The Addition of the provided numbers {self.numb1} and {self.numb2} is {self.numb1 + self.numb2}")

    def subtr(self):
        print(f"The Subtraction of the provided numbers {self.numb1} and {self.numb2} is {self.numb1 - self.numb2}")

    def mult(self):
        print(f"The Multiplication of the provided numbers {self.numb1} and {self.numb2} is {self.numb1 * self.numb2}")

    def divi(self):
        if self.numb2 != 0:
            print(f"The Division of the provided numbers {self.numb1} and {self.numb2} is {self.numb1 / self.numb2}")
        else:
            print("Error: Division by zero is not allowed.")

# Input for numbers
n1 = eval(input("Enter first number: "))
n2 = eval(input("Enter second number: "))

# Create an object of the calc class
O1 = calc(n1, n2)

# Ask user for the operation they want to perform
print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter the number corresponding to your choice: ")

# Perform the selected operation
if choice == "1":
    O1.addi()
elif choice == "2":
    O1.subtr()
elif choice == "3":
    O1.mult()
elif choice == "4":
    O1.divi()
else:
    print("Invalid choice! Please select a valid operation.")
