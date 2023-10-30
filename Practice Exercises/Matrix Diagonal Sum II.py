# Write a function to calculate the sum of the diagonals of a square matrix.
def diagonal_sum(matrix):
    n = len(matrix)
    main_diagonal_sum = sum(matrix[i][i] for i in range(n))
    anti_diagonal_sum = sum(matrix[i][n - i - 1] for i in range(n))
    return main_diagonal_sum, anti_diagonal_sum

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
main_sum, anti_sum = diagonal_sum(matrix)
print(f"Main Diagonal Sum: {main_sum}, Anti-Diagonal Sum: {anti_sum}")
