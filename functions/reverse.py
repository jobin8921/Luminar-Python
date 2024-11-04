# write a function to reverse a number 123

# def reverse_number(n):

#     i=0

#     while(n>i):        #12345   >0  True

#        digit=n%10       #5

#        print(digit,end="")    #5

#        n=n//10


# reverse_number(123)


def reverse(n1):
    rev=str(n1)[::-1]
    print(rev)
reverse(143)    