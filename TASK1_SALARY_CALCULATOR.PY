Payroll_no=int(input("ENTER YOUR PAYROLL NUMBER \n"))
Name=input("ENTER YOUR NAME \n")
Gender=input("ENTER YOUR GENDER \n")
Job_group= input("ENTER YOUR JOB GROUP \n")
Basic_salary=int(input("ENTER YOUR BASIC SALARY \n"))
match Job_group:
    case "J":
        Gross_pay=Basic_salary+5000  
        Taxes = (12*Basic_salary)/100
        Net_pay = Gross_pay - Taxes
    case "K":
        Gross_pay=Basic_salary+5500
        Taxes = (12*Basic_salary)/100
        Net_pay = Gross_pay - Taxes      
    case "L":
        Gross_pay=Basic_salary+6000
        Taxes = (12*Basic_salary)/100
        Net_pay = Gross_pay - Taxes
    case "M":
        Gross_pay=Basic_salary+6500
        Taxes = (12*Basic_salary)/100
        Net_pay = Gross_pay - Taxes        
    case _:
            print("INVAID JOB GROUP")
            exit()

print("\n*** PAYSLIP ***")
print(f"Payroll No: {Payroll_no}")
print(f"Name: {Name}")
print(f"Gender: {Gender}")
print(f"Job Group: {Job_group}")
print(f"Basic Salary: {Basic_salary}")
print(f"Gross Pay: {Gross_pay}")
print(f"Taxes: {Taxes}")
print(f"Net Pay: {Net_pay}")