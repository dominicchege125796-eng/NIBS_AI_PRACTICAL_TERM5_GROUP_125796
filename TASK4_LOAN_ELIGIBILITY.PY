Name = input("Enter Customer Name \n")
Age = int(input("Enter the age \n"))
Income =int(input("Enter your monthly income \n"))
Credit_score = int(input("Enter your credit score \n"))
if Income >= 30000 and Credit_score >= 700:
    print("Customer Name : ", Name)
    print("Approved !")
elif Income >= 30000 and Credit_score < 700:
    print("Rejected! - Credit Score is below 700")
elif Income < 30000 and Credit_score >= 700:
    print("Rejected - Income is below 30000")
elif Income < 30000 and Credit_score < 700:
    print("Both Income and Credit Score are below Expectations")
else:
    print("Invalid!")