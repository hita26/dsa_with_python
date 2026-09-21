# 23. Sort a list without using sort()
def my_sort(numbers):
    result = numbers[:]
    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            if result[i] > result[j]:
                result[i], result[j] = result[j], result[i]
    return result

print(my_sort([5, 2, 8, 1, 3]))
