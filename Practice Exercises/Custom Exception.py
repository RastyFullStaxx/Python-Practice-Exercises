class InvalidInputError(Exception):
    def __init__(self, message):
        super().__init__(message)

def calculate_square_root(number):
    if number < 0:
        raise InvalidInputError("Cannot calculate square root of a negative number")
    return number ** 0.5

try:
    result = calculate_square_root(-4)
    print(result)
except InvalidInputError as e:
    print(f"Error: {e}")
