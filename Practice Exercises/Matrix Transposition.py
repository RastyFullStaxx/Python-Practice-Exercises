# Write a function to transpose a matrix (2D list).
def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix)) ] for i in range(len(matrix[0]))]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed_matrix = transpose_matrix(matrix)
print(transposed_matrix)
