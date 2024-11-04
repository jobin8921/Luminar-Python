license = int(input("enter license number"))
license = license.strip()

if len (license) !=7:
   print("need 7 charcters")

elif license[:3].isupper() !=True:
   print("first 3 letters must be uppercase")

elif license[3:].isnumeric()!=True:
   print("need to be a number")

else:
   print("its a valid one")   