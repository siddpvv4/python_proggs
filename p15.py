#Find the greatest among two numbers
a= int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print(f"{a} is greater than {b}")
elif b > a:
    print(f"{b} is greater than {a}")
else:
    print("Both numbers are equal")