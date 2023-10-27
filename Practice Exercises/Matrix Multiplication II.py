# Implement a function to perform matrix multiplication.
def matrix_multiply(matrix1, matrix2):
    result = [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix2)] for row in matrix1]
    return result

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
result_matrix = matrix_multiply(matrix1, matrix2)
print(result_matrix)
