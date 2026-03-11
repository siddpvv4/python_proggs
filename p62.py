n = int(input("Enter number of test cases: "))

for i in range(n):
    line = input("Enter a and b: ")
    
    try:
        a, b = map(int, line.split())
        print(a // b)
        
    except ZeroDivisionError as e:
        print("Error Code:", e)
        
    except ValueError as e:
        print("Error Code:", e)