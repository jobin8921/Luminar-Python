# wap to reverse a number

n = 12345

# reversed_num = 0
# while n > 0:
#     remainder = n % 10
#     reversed_num = reversed_num * 10 + remainder
#     n = n // 10
# print(reversed_num)


i=0

while(n>i):        #12345   >0  True

    digit=n%10       #5

    print(digit,end="")    #5

    n=n//10

