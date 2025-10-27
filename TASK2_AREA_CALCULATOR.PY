import math
print("Trapizium dimensions\n")
a = int(input("Enter side a \n"))
b = int(input("Enter side b \n "))
height = int(input("Enter the height \n"))
print("Circle dimensions \n")
radius = float(input("Enter the radius of the circle \n"))
Areatrapizium = ((a+b)*height)/2
Areacircle = math.pi*radius*radius
Areashaded = Areatrapizium-Areacircle
print("Thea area of the Trapizium : ",Areatrapizium,"\n")
print("The area of the circle : ",Areacircle,"\n")
print("The area of shaded Region : ",Areashaded,"\n")