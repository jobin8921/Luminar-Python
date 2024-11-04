year = int(input("enter a year : "))

if(year%4==0) or (year%400 ==0):

    print(f"{year} its a leap year")

else:
    
    print(f"{year} its not a leap year")
