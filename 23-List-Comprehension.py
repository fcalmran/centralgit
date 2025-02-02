# List Comprehension , it is the way to define and create the list based on the existing list, you can also populate the list through the loop 

l1=[]
for a in range(1,101):
    l1.append(a)

print(l1)

# Another way , which is list comprehension...

l2=[b for b in range(1,101)] # Creating list based on comprehension...
print(l2)



# Adding conditions in comprehension like this
l3=[c for c in range(1,101) if c%2==0]
print(l3)

# Creating list based on the string given
s1="Hello World"
l4=[d for d in s1]
print(l4)




