import pytest
import random

def find_duplicate(numbers, N):
    start = 0
    end = len(numbers) - 1
    gt = 0
    le = 0
    if N == 1:
        assert len(numbers) > 1
        return numbers[0]
    while start <= end:
        if numbers[start] > N/2:
            num = numbers[end]
            numbers[end] = numbers[start]
            numbers[start] = num
            end -= 1
            gt +=1
        else:
            start +=1
            le +=1
    print le, gt, len(numbers), N
    print numbers
    assert (le + gt) == len(numbers)

    if le > N/2:
        return find_duplicate(numbers[0:le], N/2)
    elif gt > (N - N/2):
        return find_duplicate(numbers[le:], N/2)
    else:
        raise Exception("No duplicate")

if __name__ == "__main__":
    list = range(1,11)
    random.shuffle(list)
    list.append(4)
    list.append(5)
    list.append(4)
    list.append(5)
    print list

    print find_duplicate(list, 10)

