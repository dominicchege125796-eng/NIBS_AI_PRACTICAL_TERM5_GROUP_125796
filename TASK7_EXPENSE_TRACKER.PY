#TASK 7: AI-Based Expense Tracker 
#Write a Python program that: 
#•	Accepts expenses under Food, Transport, and Utilities. 
#•	Calculates total and percentage share of each. 
#•	Gives AI-based advice: 
#o 	If Food > 50% → “You are overspending on food.” o 	
# If Utilities < 20% → “Utilities spending is minimal.” • 
# 	Display data in a neat table. 

print("Enter your monthly expenses:")
    
food = float(input("Food: "))
transport = float(input("Transport: "))
utilities = float(input("Utilities: "))
    

total = food + transport + utilities

if total == 0:
        print("Total expenses cannot be zero.")
    # total percentages
food_perct = (food / total) * 100
transport_perct = (transport / total) * 100
utilities_perct = (utilities / total) * 100

    # Display table
print("\nExpense Summary:")
print("____________________")
print(f"{'Category':<12}{'Amount':>10}{'Percentage':>15}")
print("-" * 37)
print(f"{'Food':<12}{food:>10.2f}{food_perct:>14.2f}%")
print(f"{'Transport':<12}{transport:>10.2f}{transport_perct:>14.2f}%")
print(f"{'Utilities':<12}{utilities:>10.2f}{utilities_perct:>14.2f}%")
print("-" * 37)
print(f"{'Total':<12}{total:>10.2f}{'100.00%':>15}")

    # AI-based advice
print("Advice:\n")
if food_perct > 50:
        print("You are overspending on food.")
elif utilities_perct < 20:
        print(" Utilities spending is minimal.")
elif food_perct <= 50 and utilities_perct >= 20:
        print("Your spending is well balanced.")
else:
        print("too low")
print("food= ",food)
print("transport= ",transport)
print("utilities=",utilities)

