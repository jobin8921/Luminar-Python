
head = [1,2,3,4,5]

length = len(head)

i=1

while(i<length):

    head.insert(i,head.pop(-1))

    i+=2

print(head)

