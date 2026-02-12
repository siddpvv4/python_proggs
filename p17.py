#Check whether quadratic equation has real or imaginary roots
import math
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
d = b**2 - 4*a*c 
if d > 0:
    print("Roots are real and different")
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    print("Root 1 =", r1)
    print("Root 2 =", r2)

elif d == 0:
    print("Roots are real and equal")
    r = -b / (2*a)
    print("Root =", r)

else:
    print("Roots are imaginary")
    real = -b / (2*a)
    imag = math.sqrt(-d) / (2*a)
    print("Root 1 =", real, "+", imag, "i")
    print("Root 2 =", real, "-", imag, "i")
