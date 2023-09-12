def unique_paths(m, n):
    dp = [[1] * n] * m
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]

rows, cols = 3, 7
result = unique_paths(rows, cols)
print(result)
