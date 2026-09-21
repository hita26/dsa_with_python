#9. Check whether a number is prime
n = int(input("Enter a number: "))
is_prime = True

if n < 2:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime number")
else:
    print("Not a prime number")
