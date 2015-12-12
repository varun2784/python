import csv
import pytest
import sys
import math



#hashtable to store coffe shop coordinates, indexed by name
Shops = {}
#list to store euclidean distance
Distance = []

def CalculateDistance(x1, y1, x2, y2):
    return (math.sqrt((x1 - x2)**2 + (y1 - y2)**2))

def AddShop(name, x, y, user_x, user_y):
    #ignore duplicate, take first entry
    if name not in Shops:
        s = (x, y)
        Shops[name] = s
        Distance.append([name, CalculateDistance(x, y, user_x, user_y)])

def get_float(n):
    try:
        x = float(n)
    except ValueError:
        #terminate if float is not valid
        sys.exit("Malformed shop coordinate")
    return x

def get_key(item):
    # sort by distance
    return item[1]

if __name__ == "__main__":
    #check number of inputs
    if len(sys.argv) < 4:
        sys.exit("Not enough arguments")

    user_x = get_float(sys.argv[1])
    user_y = get_float(sys.argv[2])

    if user_x == None or user_y == None:
        sys.exit("Malformed user coordinates")
    
    try:
        csvfile = open(sys.argv[3])
    except IOError:
        print("CSV file not found")
    else:
        with csvfile:
            data = [AddShop(str(name), get_float(x), get_float(y), user_x, user_y) for name, x, y in csv.reader(csvfile, delimiter= ',')]
            #sort by distance
            SortedDistance = sorted(Distance, key=get_key)
            for i in range(3):
                print SortedDistance[i][0], ",", SortedDistance[i][1]


