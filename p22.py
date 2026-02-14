#Armstrong Number
num = int(input("Enter a number: "))
original = num
sum = 0

digits = len(str(num))

while num > 0:
    rem = num % 10
    sum += rem ** digits
    num //= 10

if sum == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
