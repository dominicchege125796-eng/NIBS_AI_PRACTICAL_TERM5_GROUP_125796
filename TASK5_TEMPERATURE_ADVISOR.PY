Temp = float(input("Enter the Temperature in Degrees \n"))
if Temp < 15:
    print("It's cold - Wear a jacket")
elif Temp >= 15 and Temp < 25:
    print("The weather is Pleasant - enjoy your day")
elif Temp >= 25:
    print("It's hot - stay hydrated")
else:
    print("invalid !")