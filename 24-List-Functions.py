# List Functions
    # del()
    # pop()
    # remove()
    # Clear()

l1=[10,20,30,40,50,60]
print(l1)

# using del with specific index
del l1[0]
print(l1)

del l1[0:2]
print(l1)

del l1[0::]
print(l1)

ss="Hellow Python"
l1=[a for a in ss]
print(l1)

del l1[0::2]
print(l1)

# Now using pop()

s2="123456789"
l1=[a for a in s2]
print(l1)

l1.pop(2) # You can also show what you delete is by doing this print(l1.pop(2))
print(l1)

l1.remove('4') # remember, you need to specify the value instead of the index number 
print(l1)

l1.clear()
print(l1)

# Updating the list 

l2=[20,30,40,50]
print(l2)
l2[0]=10 # remember this will replace whatever the value is present on 0 location, in this case it was 20 which is replaced so it is not insert , it is update 
print(l2)

# Functions for Updating the list are 
    # insert()
    # append()
    # extends()

# Example of Inserting the element in the given list
l3=[10,20,30,40,50,60,70]
print(l3)
l3.insert(0,5)
print(l3)


l3.insert(5,45)
print(l3)


l3.insert(9,80) # You can use insert to insert the value in the list item which is in the last place , but you can use append() which do the same 
print(l3)


l3.append(90) # the only difference is that you don't need to mention the index , becasue it know that it should place the item in last place...
print(l3)

# but what is you append the list as a item in existing list for example
l4=["A","B"]

l3.append(l4) # this will append the list as a single item 
print(l3)

print(l3[11])
l3.pop(11)
print(l3)

# Now adding the l4 contents in l3 by extending the list

l3.extend(l4)
print(l3)

# Further List Functions 
    # Count()
    # Max()
    # Min()
    # Sort()
    # reverse()
    # Index()
print("##########################################################")
l5=[10,20,30,30,30,30,40,50,50,60,60,60,60,20,20,20,10,10,60,60,70]
print(l5.count(60))
print(l5.sort()) # Shows None Why?
l5.sort()
print(l5)
# Why this ?? Reason?

# The reason print(l5.sort()) shows None is because the sort() method in Python sorts the list in place and does not return a new list. 
# Instead, it modifies the original list directly and returns None.

# Here’s a quick breakdown:

# l5.sort() sorts the list but does not return anything. It modifies l5 directly and the return value is None.
# When you try to print l5.sort(), Python prints the return value of l5.sort(), which is None, instead of the sorted list.
# To see the sorted list, you can call l5.sort() first to sort the list, and then print l5 separately:


print(max(l5))
print(min(l5))

# Same case goes with reverse, if put the print embeded with reverse function it will give None.
print(l5.reverse())
# to print it correctly we do the same method as we did in sort() function. logic is same

l5.reverse()
print(l5)

l6=["Hello","World"]
l6.reverse()
print(l6)

# Using Index Function
print(l6)
print(l6.index("Hello"))

# We can print in other way too like using variable
a=l6.index("Hello")
print(a)

# Finding the index of the item which is not exists
print(l6.index("Fun")) # Gives an error because the item doesn't exists in the list l6


