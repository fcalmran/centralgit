# List Iteration

l1=["Audi","BMW","Suzuki","Honda","Toyota","Kia","Nissan","Mercedes"]

# My Own Way to print the items from the list via loop

# But in this case you must have to hardoce the length of the list

for n in range(8):
    print(n,l1[n])

# Alternativley, you can find the length and then applied to the loop

print("################### Second Loop #############################")
ll=len(l1) # gives to the value of 8

for m in range(ll):
    print(m,l1[m])

print("################### Third Loop #############################")
# You can also print the list in loop directly passing through it

for o in l1:
    print(o)
