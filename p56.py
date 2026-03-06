#Write a Python program to create a file and write a few lines into it.
f = open("sample.txt", "w")

f.write("Hello World\n")
f.write("This is a file handling example\n")
f.write("Python is easy\n")

f.close()