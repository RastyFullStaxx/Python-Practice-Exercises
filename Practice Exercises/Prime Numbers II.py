# Create a function that generates a list of prime numbers up to a given number n.
def generate_primes(n):
    primes = []
    for num in range(2, n + 1):
        if all(num % p != 0 for p in primes):
            primes.append(num)
    return primes

print(generate_primes(30))
