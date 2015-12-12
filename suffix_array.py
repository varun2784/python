import pytest

def suffixArray(word):
    suffixs = [[word[i:], i] for i in range(len(word))]
    print suffixs
    return sorted(suffixs)

if __name__ == "__main__":
    suffixs = suffixArray("abcde")
    print suffixs
