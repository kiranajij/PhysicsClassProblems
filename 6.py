import math

def is_prime(n):
    if n == 1: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0: return False
    return True

def prime_in_range(a, b):
    primes = []
    for n in range(a, b+1):
        if is_prime(n):
            primes.append(n)
    return primes

if __name__ == '__main__':
    for i in prime_in_range(1, 100):
        print i,
