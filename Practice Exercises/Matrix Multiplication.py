def matrix_multiply(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum = 0
            for k in range(len(matrix2)):
                sum += matrix1[i][k] * matrix2[k][j]
            row.append(sum)
        result.append(row)
    return result

matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]
result_matrix = matrix_multiply(matrix_a, matrix_b)
print(result_matrix)
