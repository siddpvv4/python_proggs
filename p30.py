#123454321
#1234 *4321
#123  * * 321
#12   * * *  21
#1    * * * *   1
n = 5

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    for k in range(n - i):
        print(" *", end="")
    for j in range(i, 0, -1):
        print(j, end="")

    print()

