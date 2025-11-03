name = str(input("Enter your name \n"))
admno = int(input("Enter your Admission Number \n"))
meal_type = input("Enter your Meal type (Breakfast , Lunch, Supper)\n")
amount = int(input("Enter Payment Amount \n"))
card =1000
amount += card
if meal_type = "Breakfast":
    fee = 100
    balance = card - fee
elif meal_type = "Lunch":
    fee = 200
    balance = card - fee
elif meal_type = "Supper":
    fee = 250
    balance = card - fee
elif meal_type = "-":
    print("Invalid choice")
print("Names : " ,name)
print("Admission Number : ", admno)
print("Meal Type : ", meal_type)
print("Amount Paid : ", fee)
print("Remaining balance : ", balance)
print("Advice : ",advice)
if balance < 150:
    print("Low balance - please top-up")
elif 150 <= balance :
    print("Maintain weekly top-p schedule")

