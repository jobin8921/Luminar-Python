# check it is armstrong

# num = 153

# length = len(str(num))

# # print(length)

# # sum = 0

# # while(num>0):   # 153>0

# #     digit = num%10  #3 ** length   

# #     sum=sum+digit**length  #3**3
    
# #     num=num//10  #153//10   15//10

# #     print

    
num=456

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




