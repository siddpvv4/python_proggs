#Functions Explaining Argument Concepts
#a) Keyword Argument
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=18, name="Siddharth")
#b) Default Argument
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Rahul")
#c) Variable-length Argument
def add_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    print("Sum:", total)

add_numbers(10, 20, 30)