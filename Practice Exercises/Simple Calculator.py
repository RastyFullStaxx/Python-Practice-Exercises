# Implement a simple calculator with functions for addition, subtraction, multiplication, and division.
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

result_add = add(5, 3)
result_subtract = subtract(7, 2)
result_multiply = multiply(4, 6)
result_divide = divide(8, 2)

print(result_add, result_subtract, result_multiply, result_divide)
