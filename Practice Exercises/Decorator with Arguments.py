import functools
import time

def log_execution_time(threshold):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            if execution_time > threshold:
                print(f"{func.__name__} took {execution_time:.2f} seconds to execute")
            return result
        return wrapper
    return decorator

@log_execution_time(threshold=1.0)  # Log if execution time exceeds 1 second
def slow_function():
    time.sleep(2)

slow_function()
