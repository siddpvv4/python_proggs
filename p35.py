#Count occurrences of a substring (LEFT → RIGHT traversal)
string = input("Enter main string: ")
sub = input("Enter substring: ")
count = 0
for i in range(len(string) - len(sub) + 1):
    if string[i:i+len(sub)] == sub:
        count += 1
print(count)
