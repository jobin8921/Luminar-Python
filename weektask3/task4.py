num=153

temp=num

length=len(str(num))

sum=0

while(num>0):

    digit=num%10

    sum=sum+digit**length

    num=num//10



if sum==temp:

    print(f"{temp} is armstrong") 

else:

    print(f"{temp} is not armstrong")

