s1 = float(input("Enter the first side of the triangle : "))
s2 = float(input("Enter the second side of the triangle : "))
s3 = float(input("Enter the third side of the triangle : "))


p = (s1 + s2 + s3)

s = p/2


area = (s * (s-s1) * (s-s2)*(s-s3))**0.5


print("The perimeter of the triangle is : {0:.2f}".format(p))
print("The area of the triangle is : {0:.2f}".format(area))
print()
print()
#==============================================================================
PI = 3.14
radius = float(input(' Please Enter the radius of a circle: '))
 
diameter = 2 * radius
circumference = 2 * PI * radius
area = PI * radius * radius
 
print(" \nDiameter Of a Circle = %.2f" %diameter)
print(" Circumference Of a Circle = %.2f" %circumference)
print(" Area Of a Circle = %.2f" %area)