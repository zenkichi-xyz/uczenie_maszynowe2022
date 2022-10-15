def merge(list1: list, list2: list) -> list:
    merged = list(set(list1 + list2))
    for i in range(len(merged)):
        merged[i] = merged[i]**3
    return merged

print(merge([1, 2, 3], [2, 3, 4]))