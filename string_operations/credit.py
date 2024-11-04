
credit_score = int(input("enter ur credit score : "))

if credit_score < 580:    #500 < 580
    print("you are poor")

elif credit_score > 580 and  credit_score < 669:         
    print("you are fair")

elif credit_score > 670 and credit_score < 669:
    print("you are good")

elif credit_score > 740 and credit_score <= 799:
    print("you are very good")

else:
    print("ur exceptioanl")    