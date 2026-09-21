# 15. Sum of all elements in a list
def list_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(list_sum([10, 20, 30, 40]))
