def spiral_order(matrix):
    result = []
    while matrix:
        result += matrix[0]
        matrix = list(zip(*matrix[1:]))[::-1]
    return result

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
spiral = spiral_order(matrix)
print(spiral)
