


height_incm = int(input("enter ur height"))

weight_inkg = int(input("enter ur weight"))

height_m = height_incm/100

bmi = weight_inkg/(height_m)**2
print(bmi)
if bmi < 18:

    print("ur are under weight") 

elif bmi >= 18 and bmi <=24:     #18 -24

    print("Normal weight")       

elif bmi > 24 and bmi <=30:     # 24    - 30

    print("ur are over weight")

else:
    print("ur are obese")


