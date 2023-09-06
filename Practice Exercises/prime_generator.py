def prime_generator():
    primes = []
    num = 2
    while True:
        if all(num % prime != 0 for prime in primes):
            yield num
            primes.append(num)
        num += 1

prime_gen = prime_generator()
for _ in range(10):
    print(next(prime_gen))
