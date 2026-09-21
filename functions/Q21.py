# 21. Fibonacci numbers
def fibonacci(n):
    numbers = []
    a, b = 0, 1
    for i in range(n):
        numbers.append(a)
        a, b = b, a + b
    return numbers

print(fibonacci(10))
