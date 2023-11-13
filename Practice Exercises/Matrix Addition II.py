# Write a function to perform matrix addition.
def matrix_addition(matrix1, matrix2):
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return result

matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]
matrix_sum = matrix_addition(matrix_a, matrix_b)
print(matrix_sum)
