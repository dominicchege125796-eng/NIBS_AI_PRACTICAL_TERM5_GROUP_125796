import cmath
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate the discriminant
D = cmath.sqrt(b**2 - 4*a*c)

# Calculate the two solutions
x1 = (-b + D) / (2*a)
x2 = (-b - D) / (2*a)

print("The solutions are: ",x1,"or",x2)