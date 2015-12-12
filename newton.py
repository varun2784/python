import pytest
import sys

def cuberoot(n):
    approx = 0.1 * n
    better = (2 * approx + n / (approx ** 2)) * 0.333333
    while better != approx:
        approx = better
        better = (2 * approx + n / (approx ** 2))/3
    return better

def sqroot(n):
    approx = 0.1 * n
    better = 0.5 * (approx + n / approx)
    while better != approx:
        approx = better
        better = 0.5 * (approx + n / approx)
    return better

if __name__ == "__main__":
    try:
        num = float(sys.argv[1])
        print cuberoot(float(sys.argv[1]))
    except:
        raise Exception("invalid input")
