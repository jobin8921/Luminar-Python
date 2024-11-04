#check wheather 
# number is divsible by both 3 and 5
# a number eitehr by 3 or 5
#not disvible by with 3 and 5

num = int(input("enter the number "))

# if num % 3 == 0  and  num % 5 == 0:

#     print(f"{num} is divisble by both 3 and 5")

# elif num%3 ==0 or num% 5 ==0:

#     print(f"{num} is divisible by either 3 or 5")
    

# else:

#     print(f"{num} not  divsisble with 3 amd 5")   


result = "is divisble" if num % 3==0 and num % 5==0 else("is divisble with either 3 and 5" if num%3 ==0 or num% 5==0 else"not divisble by 3 and 5" )
print(result)
