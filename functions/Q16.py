# 16. Largest element in a list
def largest(numbers):
    biggest = numbers[0]
    for n in numbers:
        if n > biggest:
            biggest = n
    return biggest

print(largest([12, 45, 23, 67, 34]))
