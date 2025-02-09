l=[]
while True:
    c=int(input('''
    1 Push Elements
    2 Pop Elements
    3 Peek Elements
    4 Display Stack
    5 Exit        

                '''
                ))
    if c==1:
     n=input("Enter the Value... > ")
     l.append(n)
     print(l)
    elif c==2:
       if len(l)==0:
          print("List is empty...")
       else:
            popitem=l.pop()
            print(popitem)
            print(l)
    elif c==3:
       print(l[-1])
    elif c==4:
       print(l)
    elif c==5:
       break


