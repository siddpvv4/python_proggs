#Read and display the contents of a file.
f = open("data.txt", "r")
content = f.read()
print(content)
f.close()