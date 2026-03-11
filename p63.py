try:
    with open("counter.txt", "r") as f:
        count = int(f.read())

except FileNotFoundError:
    count = 0

except ValueError:
    count = 0

except PermissionError:
    print("Error: No permission to access file.")
    exit()

except Exception as e:
    print("Unexpected Error:", e)
    exit()

count += 1

try:
    with open("counter.txt", "w") as f:
        f.write(str(count))

except PermissionError:
    print("Error: No permission to write to file.")
    exit()

except Exception as e:
    print("Unexpected Error:", e)
    exit()

print("Program has been executed", count, "times.")