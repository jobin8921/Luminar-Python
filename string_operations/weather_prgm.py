weather_today = input("is it rainy today: ")  

weather_today = weather_today.lower()

if weather_today == "yes":

    windy_check =input("is it windy today : ")

    if windy_check == "yes":
        print("it is too windy for a umberalla : ")
    else:
        print("take umbrella")

else:

    print("enjoy ur day")
       