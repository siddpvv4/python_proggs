# Average of a Tuple (Easy Version)
n = int(input("Enter the number of numeric values: "))
numbers = [] 
for i in range(n):
    val = float(input("Enter value " + str(i+1) + ": "))
    numbers.append(val)


num_tuple = tuple(numbers)


if n > 0:
    total = sum(num_tuple)
    average = total / n

    print("\nTuple created:", num_tuple)
    print("Average of all values:", average)
else:
    print("No values entered.")
