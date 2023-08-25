import functools
import time

def log_function_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        print(f"Function: {func.__name__}")
        print(f"Arguments: {args}, {kwargs}")
        print(f"Return value: {result}")
        print(f"Execution time: {(end_time - start_time) * 1000:.2f} ms\n")

        return result

    return wrapper

# Usage
@log_function_call
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Test the decorated function
print(fibonacci(5))
