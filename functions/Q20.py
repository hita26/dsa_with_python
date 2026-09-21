# 20. Prime numbers between two numbers
def primes_between(start, end):
    primes = []
    for n in range(start, end + 1):
        if is_prime(n):
            primes.append(n)
    return primes

print(primes_between(10, 30))
 
