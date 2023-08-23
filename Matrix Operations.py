def matrix_multiply(matrix1, matrix2):
    result = []
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])

    if cols1 != rows2:
        raise ValueError("Matrix dimensions are incompatible for multiplication")

    for i in range(rows1):
        row = []
        for j in range(cols2):
            element = sum(matrix1[i][k] * matrix2[k][j] for k in range(cols1))
            row.append(element)
        result.append(row)

    return result

# Test the function
matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]
result_matrix = matrix_multiply(matrix_a, matrix_b)
print(result_matrix)
