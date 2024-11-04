# count of odd digits in the number enter ny user

num = int (input("enter the number : "))    #12345
 
count = 0     
     
for i in str(num):              

    if int(i)%2!= 0:

        count=count+1

print(count)





