# sum of square of even digits   in a number


number = int(input("enter the number"))

sum =0

for i in str(number):

    if int(i)%2==0:


        sum=sum +  int(i)**2

print(sum)




    
