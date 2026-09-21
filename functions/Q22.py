# 22. Second-largest number in a list
def second_largest(numbers):
    unique = list(set(numbers))
    unique.sort(reverse=True)
    return unique[1]

print(second_largest([10, 25, 40, 30, 40]))
