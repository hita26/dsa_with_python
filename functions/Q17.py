# 17. Remove duplicate elements
def remove_duplicates(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
