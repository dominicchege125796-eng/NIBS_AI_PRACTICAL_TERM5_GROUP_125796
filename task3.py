Name = input("Enter student's Names \n")
print("Enter marks for the three Subjects")
marks1 = int(input())
marks2 = int(input())
marks3 = int(input())
sum = marks1 + marks2 + marks3
average = sum/3
print("Name : ",Name)
print("Average : ",average)
if average>=80 and average<100:
    print("Grade : A")
elif average>=70 and average<80:
    print("Grade : B")
elif average>=60 and average <70:
    print("Grade : C")
elif average>=50 and average<60:
    print("Grade : D")
elif average <50:
    print("FAIL!")
else:
    print("Invalid Marks")


