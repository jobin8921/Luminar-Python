#write a functionthat reverses the order of words in a given sentences but keeps the vharacters in each word in the correct order.
#eg   :"hello world"  == "world hello"



# def reverse (a):

#     rev=0

#     string=str(a)

#     while(a>0):

#         digit=a%10
#         rev=rev*10+digit
#         a=a//10
#     print(f"{rev}")

# reverse("hello world")




#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#write a function that takes a  positive integer  n returns the sum of digits



# def positive(n):
#     sum=0

#     while(n>0):

#       digit=n%10

#       sum=sum+digit

#       n=n//10
#     print(sum)

#     if n>0:

#         print(f"positive")

#     else:

#          print(f"negative")
# positive(246)



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def reverse(n):
   
   rev=0

   while(n>0):

      digit=n%10

      rev=rev*10+digit

      n=n//10

   print(rev)
    
reverse(12)



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#write a function return sum of the first n natural numbers using the formula sum=n(n+1)/2










#create  a function to check entered character is vowel or consonant


















#wap to find the primr numbers below n where n is entered bythe user























##wap to print the characters of  a string in even positions >>>>> namw =python =o/p=y h n

















#wap to print sum of even and odd indexed digits in a given number


def sum(n):

   if n%2==0:

      print(f" {n} even")

   else:

      print(f" {n}odd")

sum()