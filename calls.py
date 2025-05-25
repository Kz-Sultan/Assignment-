def greet(name):
    print(f"Hello, {name}!")

def add_numbers(a, b):
    return a + b

def is_even(number):
    return number % 2 == 0

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Calling functions
greet("Sultan")
print("Sum:", add_numbers(10, 5))
print("Is 7 even?", is_even(7))
print("Factorial of 4:", factorial(4))