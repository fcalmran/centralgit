w1="Welcome {} to the world of Python {}".format("!",", Yupee")
print(w1)

w2="Welcome{1} to the world of Python {0}".format("Ponka","Chal Nikal") # Using index number to postion the value in a string
print(w2)


w3="Welcome {b} to the world of Python {a}".format(a=10,b=20)
print(w3)

w4="Welcome to {a:10} to the workd of PYTHON {b} ".format(a=50,b=60) # Padding the space in a and the total length would be 10 , so a occupies 2 remaining will be empty showed
print(w4) # Default align right

w5="Welcome to {a:10} to the workd of PYTHON {b:^10} ".format(a=50,b=60) # Padding the space in b and the total length would be 10 , so a occupies 2 remaining will be empty showed
print(w5) # ^ align the text in center

w6="Welcome to {a:<10} to the workd of PYTHON {b:^10} ".format(a=50,b=60) # Padding the space in b and the total length would be 10 , so a occupies 2 remaining will be empty showed
print(w6) # ^ align the text in Left

w7="Welcome to {a:>10} to the workd of PYTHON {b:^10} ".format(a=50,b=60) # Padding the space in b and the total length would be 10 , so a occupies 2 remaining will be empty showed
print(w7) # ^ align the text in cRight
