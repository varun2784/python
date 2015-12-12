import pytest

def bsearch(list_items, key):
    if len(list_items) == 0:
        return -1
    print list_items
    mid = len(list_items)/2
    if key == list_items[mid]:
        return mid
    elif key < list_items[mid]:
        print "Searching left for", key, "in", list_items[:mid]
        return bsearch(list_items[:mid], key)
    else:
        print "Searching right for", key, "in", list_items[mid+1:]
        return bsearch(list_items[mid + 1:], key)

if __name__ == "__main__":
    nos = range(10)
    for i in [x**2 for x in range(4)]:
        found = bsearch(nos, i)
        if found != -1:
            print i, "found at", found
        else:
            print i, "not found"
