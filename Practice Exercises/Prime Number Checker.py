def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

num1 = 17
num2 = 12
print(f"{num1}: {is_prime(num1)}")
print(f"{num2}: {is_prime(num2)}")
