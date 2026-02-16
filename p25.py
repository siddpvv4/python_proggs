#Palindrome Number Check
num = int(input("Enter a number: "))
original = num
rev = 0

while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num //= 10

if rev == original:
    print("Palindrome Number")
else:
    print("Not a Palindrome")
