#Dictionary of Students and Cities
n = int(input("Enter the number of persons: "))
students = {}

for i in range(n):
    name = input("Enter student name: ")
    city = input("Enter city: ")
    students[name] = city

print("\na) All names:")
print(list(students.keys()))

print("\nb) All city names:")
print(list(students.values()))

print("\nc) Student name and city of all students:")
for name, city in students.items():
    print(f"{name} lives in {city}")

print("\nd) Number of students in each city:")
city_counts = {}
for city in students.values():
    
    city_counts[city] = city_counts.get(city, 0) + 1

for city, count in city_counts.items():
    print(f"{city}: {count}")