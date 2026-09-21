# 24. Merge two lists and remove duplicates
def merge_lists(list1, list2):
    result = []
    for item in list1 + list2:
        if item not in result:
            result.append(item)
    return result

print(merge_lists([1, 2, 3], [3, 4, 5]))
