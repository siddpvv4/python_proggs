#Sum of Digits
num = int(input("Enter a number: "))
sum_digits = 0

while num > 0:
    rem = num % 10
    sum_digits += rem
    num //= 10

print("Sum of digits =", sum_digits)
