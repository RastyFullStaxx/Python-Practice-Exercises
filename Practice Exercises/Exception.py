class MyCustomException(Exception):
    pass

def some_function():
    raise MyCustomException("This is a custom exception")

try:
    some_function()
except MyCustomException as e:
    print(e)
