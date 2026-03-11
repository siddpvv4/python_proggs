# Write city data
with open("city.txt", "w") as f:
    f.write("Dehradun 5.78 308.20\n")
    f.write("Delhi 190 1484\n")
    f.write("Mumbai 209 603.40\n")
    f.write("Bangalore 130 741\n")
    f.write("Jaipur 38 467.02\n")

# Read city data
with open("city.txt", "r") as f:
    cities = [line.strip().split() for line in f if line.strip()]

print("All cities:")
for city in cities:
    print(f"City: {city[0]}, Population: {city[1]} Lakhs, Area: {city[2]} sq KM")

print("\nCities with population more than 10 lakhs:")
for city in cities:
    if float(city[1]) > 10:
        print(city[0])

# Sum of areas
total_area = sum(float(city[2]) for city in cities)
print("\nSum of areas of all cities:", total_area, "sq KM")