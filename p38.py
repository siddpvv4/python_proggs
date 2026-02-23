#Two sets of fruits
n = int(input("Enter number of fruits in each set: "))
s1 = set()
s2 = set()
print("Enter fruits for set 1:")
for i in range(n):
    s1.add(input())

print("Enter fruits for set 2:")
for i in range(n):
    s2.add(input())

print("Common fruits:", s1 & s2)


print("Only in s1:", s1 - s2)


print("Total unique fruits:", len(s1 | s2))
