def factorial_with_memoization(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    result = n * factorial_with_memoization(n - 1, memo)
    memo[n] = result
    return result

num = 6
print(factorial_with_memoization(num))
