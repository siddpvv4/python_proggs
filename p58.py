#Read File Line by Line
f = open("data.txt", "r")

for line in f:
    print(line.strip())

f.close()