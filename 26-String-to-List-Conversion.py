
i=input("Enter the String to be converted...> ")
print(i)

# This will create a list l by using split() , basically it splitting the string provided and assign it to list l
l=i.split()
print(l)
print(type(l))

# Another Program
l2=[] # Initially the list  is empty
for a in range(1,4):
    n=input("Enter the value "+str(a)+":- ")
    l2.append(n)
print(l2)
 