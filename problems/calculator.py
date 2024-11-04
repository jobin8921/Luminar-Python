num1 = int(input("enter the first number : "))

num2 = int(input("enter the second number : "))

operator = input("enter the operator : ")

if operator == "+":

    sum=num1 + num2
    print(f"{num1} and {num2} is {sum}")

elif operator =="-":
    sub = num1 - num2
    print(f"{num1} and {num2} is {sub}")
      
elif operator =="*":
    print(f"{num1} and {num2} is {num1 * num2} ")

elif operator == "/":
    div = num1 / num2
    print(f"{num1} and {num2} is {div}")

else:
    print("enter a valid operator")


