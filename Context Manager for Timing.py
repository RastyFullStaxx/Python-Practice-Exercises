import time

class TimerContext:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        execution_time = (self.end_time - self.start_time) * 1000
        print(f"Execution time: {execution_time:.2f} ms")

# Usage
with TimerContext():
    # Code block to measure
    for _ in range(1000000):
        _ = 2 * 2
