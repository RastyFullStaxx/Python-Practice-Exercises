# Write a Python function to generate the Fibonacci sequence up to a given number n.
def fibonacci(n):
    fib = [0, 1]
    while fib[-1] + fib[-2] <= n:
        fib.append(fib[-1] + fib[-2])
    return fib

print(fibonacci(100))
