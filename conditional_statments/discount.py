quantity = int(input("Enter your purchase quantity: "))
cost = quantity * 100
print(cost)

if cost > 1000 :
    
    print("you got discount of 10% ")
    discount_price = cost-(cost * 10/100)
    print(discount_price)
else:

    print(f"Total amount :{cost}")