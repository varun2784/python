import random

def qsort_python(keys):
    if not keys:
        return []
    rindex = random.randint(0, len(keys)-1)
    pivot = [keys[rindex]]
    less = [x for x in keys if x < keys[rindex]]
    more = [x for x in keys if x > keys[rindex]]
    return less + pivot + more

def qsort(keys):
    if not keys:
        return []
    items = len(keys)
    if items == 1:
        return keys
    rindex = random.randint(0, items-1)
    rval = keys[rindex]
    keys[rindex] = keys[0]
    keys[0] = rval
    end = items - 1
    start = 1
    while start <= end:
        cur = keys[start]
        if cur > rval:
            keys[start] = keys[end]
            keys[end] = cur
            end -= 1
        else:
            start += 1
    keys[0] = keys[start - 1]
    keys[start - 1] = rval
    less = qsort(keys[:start - 1])
    more = qsort(keys[start:])
    return less + [keys[start - 1]] + more

if __name__ == "__main__":

    keys = range(20)
    random.shuffle(keys)
    print keys
    sorted = qsort_python(keys)
    print sorted
    


