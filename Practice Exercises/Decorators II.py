# Implement a decorator that measures and prints the execution time of a function.
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to execute.")
        return result
    return wrapper

@measure_time
def some_function():
    # Your code here
    pass
