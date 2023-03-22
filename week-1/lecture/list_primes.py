def get_primes(n):
    primes = []
    for num in range(2, n+1):
        is_prime = True
        for factor in range(2, num):
            if num % factor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

def sieve_of_eratosthenes(n):
    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if it is Not a prime, else true.
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
            # Update all multiples of p
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
    # Return all prime numbers
    primes = []
    for p in range(2, n+1):
        if prime[p]:
            primes.append(p)
    return primes


import timeit

n = 10000

result = timeit.timeit(stmt='get_primes(n)', globals=globals(), number=1)
print(f"Execution time is {result} seconds")

result = timeit.timeit(stmt='sieve_of_eratosthenes(n)', globals=globals(), number=1)
print(f"Execution time is {result} seconds")

