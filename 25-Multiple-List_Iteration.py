# How to iterate multiple list


# Traditional Way
l1=[10,30,50,70,90]
l2=[20,40,60,80,100]

ln=len(l1)

for a in range(ln):
    print(a,l1[a],l2[a])

# Using Zip() Function to iterate multiple lists or tuples etc
print("########### Using Function ###############")
for a,b in zip(l1,l2):
    print(a,b)
# let's say we have to iterate 4 lists 

print("Checking 4 lists iteration .....")
l3=[110,130,150,170,190]
l4=[120,140,160,180,200]

for q,w,e,r in zip(l1,l2,l3,l4):
    print(q,w,e,r)

# Keep in mind if the list have different length then it won't print the extra length items for example
l5=[1,2,3,4]
l6=[1,2,3]

for a,b in zip(l5,l6):
    print(a,b) # Note it will not print the last item in l5=4 because it is additional in length so the zip function discarded or ignore the value 
