mark=int(input("enter the grade : "))

if mark >= 80:     
    print("Grade is A")

elif mark >= 60 and mark <= 80:
    print("Grade is B")

elif mark >= 50 and mark <= 60:
    print("Grade is C") 

elif mark >= 45 and mark <= 50:
    print("Grade is D")

elif mark >= 25 and mark <=45:
    print("Grade is E")
    
else:
    print("Grade is F")  