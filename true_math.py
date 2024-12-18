from math import inf

def divide(first, second):
    if second == 0:
        return inf
    return int(first) / int(second)
