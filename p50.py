#recursive Fibonacci Series up to n Terms
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def print_fibonacci_terms(n):
    for i in range(n):
        print(fibonacci(i), end=" ")


# Example
print_fibonacci_terms(7)