import pytest

def permutation(list_s, start):
    len_s = len(list_s)
    if start == len_s - 1:
        print list_s
        return
    assert start <= (len_s - 1)
    for i in range(start, len_s):
        x = list_s[start]
        list_s[start] = list_s[i]
        list_s[i] = x
        permutation(list_s[:], start + 1) 

if __name__ == "__main__":
    permutation(['a', 'b', 'c', 'd', 'e'], 0)

