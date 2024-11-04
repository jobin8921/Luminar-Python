# wap t find sum of numbers from 1 to n

i=1

n = int(input("enter the value : "))

sum=0

while(i<=n):

    # if i<5:
    #     print(i,end="+")
    # else:
    #     print(i,end="")    

    sum=sum+i
     
    i=i+1

print(f" = {sum}")
