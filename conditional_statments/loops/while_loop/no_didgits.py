# wap to print the no of didgits  in the number enter by user >>>>>

n = int(input("Enter the number : "))

no_of_digits = 0

while(n>0):

    digit = n % 10 

    no_of_digits+=1

    n=n//10

print(no_of_digits)



