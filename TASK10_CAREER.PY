print("WELCOME TO CAREER RECOMMENDATION SYYSTEM")
print("=====================================")
name=input("ENTER YOUR NAME:\n")
prefsubject=input("ENTER YOUR PREFERRED SUBJECT:\n")
if prefsubject=="maths":
    print("HELLO", name,"YOU CAN BE A DATA ANALYST OR ENGINEER")
elif prefsubject=="science":
    print("HELLO", name,"YOU CAN BE A LAB TECHNICIAN OR RESEARCHER")
elif prefsubject=="art":
    print("HELLO", name,"YOU CAN BE AN ART DESIGNER OR ANIMATOR")
elif prefsubject=="business":
    print("HELLO", name,"YOU CAN BE A MARKETER OR ACCOUNTANT")
elif prefsubject=="home science":
    print("HELLO", name,"YOU CAN DO CATERING AND ACCOMMODATION")
else:
    print("OOPS!,THERE IS NO COURSE FOR THIS UNIT.")