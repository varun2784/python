import pytest
import random

def merge(left, right):
    i = 0
    j = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged

def mergeSort(keys):
    l = len(keys)
    if (l == 1):
        return keys
    mid = l/2
    left = mergeSort(keys[:mid])
    right = mergeSort(keys[mid:])
    return merge(left, right)

if __name__ == "__main__":
    nos = range(1000)
    random.shuffle(nos)
    print nos
    nos_sorted = mergeSort(nos)
    print nos_sorted
