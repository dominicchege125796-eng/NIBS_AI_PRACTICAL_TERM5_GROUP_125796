Age = int(input("Enter your age \n"))
if Age < 13:
    print("Child")
elif Age >= 13 and Age <= 19:
    print("Teenager")
elif Age >= 20 and Age <= 59:
    print("Adult")
elif Age >= 60:
    print("Senior")