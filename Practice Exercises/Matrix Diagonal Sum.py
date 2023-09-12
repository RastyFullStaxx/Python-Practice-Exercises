def diagonal_sum(matrix):
    n = len(matrix)
    primary_sum = sum(matrix[i][i] for i in range(n))
    secondary_sum = sum(matrix[i][n - i - 1] for i in range(n))
    return primary_sum + secondary_sum

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = diagonal_sum(matrix)
print(result)
