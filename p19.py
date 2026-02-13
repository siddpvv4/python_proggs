#Program to display next date
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    days_in_month[1] = 29

day += 1

if day > days_in_month[month - 1]:
    day = 1
    month += 1

    if month > 12:
        month = 1
        year += 1

print("Next Date is:", day, "/", month, "/", year)
