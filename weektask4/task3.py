for row in range(1,5):
    for col in range(4,row-1,-1):
        print("*", end=" ")
    print()    

for row in range(2,5):
    for col in range(1, row+1):
        print("*", end=" ")
    print()    
