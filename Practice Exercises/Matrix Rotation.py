def rotate_matrix(matrix):
    n = len(matrix)
    rotated = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n - i - 1] = matrix[i][j]
    return rotated

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotated_matrix = rotate_matrix(matrix)
for row in rotated_matrix:
    print(row)
