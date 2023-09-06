def fibonacci_with_memoization(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    result = fibonacci_with_memoization(n - 1, memo) + fibonacci_with_memoization(n - 2, memo)
    memo[n] = result
    return result

n = 10
fib_number = fibonacci_with_memoization(n)
print(f"The {n}-th Fibonacci number is {fib_number}")
