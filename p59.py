# Write names into a file
with open("name.txt", "w") as f:
    f.write("Alice\nBob\nEvan\nLiam\nMike\nUma\n")

# Read names from file
with open("name.txt", "r") as f:
    names = [line.strip() for line in f if line.strip()]

# Number of names
print("Number of names:", len(names))

# Names starting with vowel
vowels = "AEIOUaeiou"
count = sum(1 for name in names if name[0] in vowels)
print("Names starting with vowel:", count)

# Longest name
longest = max(names, key=len)
print("Longest name:", longest)