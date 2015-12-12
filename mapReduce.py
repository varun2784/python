if __name__ == "__main__":
    numbers = range(10)
    numbers_filtered = filter(lambda x: x%2 == 0, numbers)
    final = reduce(lambda x,y : x+y, map(lambda x: x, numbers_filtered))
    print final
