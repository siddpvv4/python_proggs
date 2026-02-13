#Grade Sheet Program (Marks → Percentage → CGPA → Grade)
name = input("Enter student name: ")
roll = input("Enter roll number: ")
sapid = input("Enter SAP ID: ")

print("\nEnter marks of five subjects:")

m1 = int(input("PDS: "))
m2 = int(input("Python: "))
m3 = int(input("Chemistry: "))
m4 = int(input("English: "))
m5 = int(input("Physics: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5
cgpa = percentage / 10

if cgpa <= 3.4:
    grade = "F"
elif cgpa <= 5.0:
    grade = "C+"
elif cgpa <= 6.0:
    grade = "B"
elif cgpa <= 7.0:
    grade = "B+"
elif cgpa <= 8.0:
    grade = "A"
elif cgpa <= 9.0:
    grade = "A+"
else:
    grade = "O (Outstanding)"

print("\n-------- Grade Sheet --------")
print("Name:", name)
print("Roll Number:", roll, "\tSAPID:", sapid)

print("\nSubject Marks:")
print("PDS:", m1)
print("Python:", m2)
print("Chemistry:", m3)
print("English:", m4)
print("Physics:", m5)

print("\nPercentage:", percentage, "%")
print("CGPA:", round(cgpa, 2))
print("Grade:", grade)
