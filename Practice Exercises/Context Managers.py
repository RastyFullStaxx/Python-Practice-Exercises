class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
        if exc_type is not None:
            print(f"An exception of type {exc_type} occurred with value {exc_value}")
        return False

with MyContextManager() as cm:
    # Your code here
    pass
