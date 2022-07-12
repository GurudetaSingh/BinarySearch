import random
import time

# Normal search scans entire list to check if value is equal to target
def normal_search(x, target):
    for i in range(len(x)):
        if x[i] == target:
            return i
    return - 1

# Binary search uses divide and conquer
def binary_search(x, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(x) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2 # Floor division to get middle of list

    # If midpoint equal to target, return target
    if x[midpoint] == target:
        return midpoint
    # If target less than midpoint, check left side of list
    elif target < x[midpoint]:
        return binary_search(x, target, low, midpoint-1)
    # Otherwise target is greater, check right side of list
    else:
        return binary_search(x, target, midpoint+1, high)

if __name__=='__main__':
    x = [1, 3, 4, 6, 9, 12]
    target = 6
    print(normal_search(x, target))
    print(binary_search(x, target))