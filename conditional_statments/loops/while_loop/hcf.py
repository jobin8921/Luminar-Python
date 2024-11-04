
num1 = int(input("enter the first number : "))

num2 = int(input("enter the second number : "))

smallest = num1 if num1<num2 else num2


i= 1

hcf = 0

while(i<=smallest):


    if num1%i==0 and num2%i==0:

        hcf = i

    i=i+1


print(f"the highest common factor of {num1} and {num2} is {hcf}")    