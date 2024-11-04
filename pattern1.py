
# for i in range(5,0,-1):

#     print(i,end=" ")

# for row in range(1,5):
#     for col in range(1,5):
#         print(col,end=" ")
#     print()

for row in range(5,0,-1):
    for col in range(5,row-1,-1):
        print(row,end="\t")
    print()    