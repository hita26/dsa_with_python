# 18. Count how many times an element appears
def count_element(items, value):
    count = 0
    for item in items:
        if item == value:
            count += 1
    return count

print(count_element([1, 2, 2, 3, 2, 4], 2))
