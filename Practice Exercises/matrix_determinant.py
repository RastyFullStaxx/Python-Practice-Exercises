def matrix_determinant(matrix):
    if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
        raise ValueError("Input must be a 2x2 matrix.")
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

matrix = [[2, 3], [1, 4]]
determinant = matrix_determinant(matrix)
print(determinant)
