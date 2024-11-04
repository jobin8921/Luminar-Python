#check wheather number positive negative 0


num = int(input("enter :"))

if num > 0:

    print("number is positive")

elif num==0:
    
    print("number is zero")

else:

    print("number is negative")

result = "number is positive" if num >0 else ("negative" if num <0 else "its a zero")    

print(result)