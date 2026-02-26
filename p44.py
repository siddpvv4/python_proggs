#Movie Details Manager
n = int(input("Enter the number of movies: "))
movies = {}

for _ in range(n):
    name = input("\nEnter movie name: ")
    year = int(input("Enter release year: "))
    director = input("Enter director name: ")
    cost = float(input("Enter production cost: "))
    earning = float(input("Enter collection made (earning): "))
    
    # Storing details as a dictionary inside the main dictionary
    movies[name] = {
        'year': year, 
        'director': director, 
        'cost': cost, 
        'earning': earning
    }

print("\n--- a) All Movie Details ---")
for name, details in movies.items():
    print(f"Movie: {name} | Details: {details}")

print("\n--- b) Movies released before 2015 ---")
for name, details in movies.items():
    if details['year'] < 2015:
        print(name)

print("\n--- c) Movies that made a profit ---")
for name, details in movies.items():
    if details['earning'] > details['cost']:
        print(name)

print("\n--- d) Movies directed by a particular director ---")
search_director = input("Enter the name of the director to search: ")
found = False
for name, details in movies.items():
    if details['director'].lower() == search_director.lower():
        print(name)
        found = True
if not found:
    print("No movies found by that director.")