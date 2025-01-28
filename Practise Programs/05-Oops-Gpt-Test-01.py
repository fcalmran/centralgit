# ANSWER - 01
class Person():

    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def greet(self):
        print(f"Hello {self.name}, you are {self.age} year old")
    


a=Person("Jason",50)
a.greet()

# ANSWER - 02 

class Book():
    
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    
    def info(self):
        print(f"The Book {self.title} written by {self.author} has a price of only {self.price} Rupees")

title=input("Enter the name of the book")
author=input("Enter the author name")
price=eval(input("Enter the price"))

b1 = Book(title,author,price)
b1.info()

# ANSWER - 03

class Rectangle():

    def __init__(self,length,width):
        self.lenght=length
        self.width=width
    
    def Area(self):
        print(f"The area of the given rectangle whose length is {self.lenght} and width is {self.width}.. ",self.lenght*self.width)

R1 = Rectangle(15,10)
R1.Area()    

# ANSWER - 04

class Circle():

    def __init__(self,radius):
        self.pi=3.142
        self.radius=radius
    
    def calculate_circumference(self):
        print(f"The circumfere of the circle that has raius {self.radius}",2*self.pi*self.radius)

radius=eval(input("Enter the radius of the circle   "))

c1 = Circle(radius)
c1.calculate_circumference()

# ANSWER - 05

class Counter():
    count=0

    def increement(self):
        self.count=0
        while self.count<=15:
            print(f"The Counter value is {self.count}")
            self.count+=1
        
    def decrement(self):
        self.count=15
        while self.count>=0:
            print(f"The Counter value is {self.count}")
            self.count-=1

    def reset(self):
        self.count=0
        print(f"The counter has been reset, and it's value is {self.count}")

    def display(self):
        print(f"The value of the counter is {self.count}")


O1 = Counter()
O1.increement()
O1.decrement()
O1.reset()
O1.display()

# or
# # ANSWER - 05

class Counter():
    count=0

    def increement(self):
        self.count+=1
        print(f"The Counter value is {self.count}")
              
    def decrement(self):
        self.count-=1
        print(f"The Counter value is {self.count}")
    
    def reset(self):
        self.count=0
        print(f"The counter has been reset, and it's value is {self.count}")

    def display(self):
        print(f"The value of the counter is {self.count}")


O1 = Counter()
O1.increement()
O1.decrement()
O1.reset()
O1.display()
