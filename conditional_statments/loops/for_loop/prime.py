

# num = 7

# for i in range(2,num):  
#     if num % i == 0:
#         print(f"{num} is not a prime number")
#         break

# else:
     
#     print(f"{num} is a prime number")


# ask to enter number from user and checkit is prime
num = int(input("Enter a number: "))
for i in range(2,num):
    if num == 1:

        print("enter a number greater than 1")
        print(f"{num} is not a prime number")
        break
else:
    print(f"{num} is a prime number")


    