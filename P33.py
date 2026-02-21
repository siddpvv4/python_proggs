#Count total number of vowels
s = input("Enter a string: ")
count = 0
for ch in s:
    if ch in "aeiouAEIOU":
        count += 1
print("Total vowels =", count)
