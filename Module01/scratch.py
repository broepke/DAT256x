import math

def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

n = 16
i = 2

while i * i < n:
    while n%i == 0:
        n = n / i
    i = i + 1

print (n)

n = 16

print(largest_prime_factor(n))
print(prime_factors(n))
